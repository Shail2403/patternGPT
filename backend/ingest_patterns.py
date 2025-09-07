"""
Ingest pattern_codeDB.py into persistent ChromaDB collection.
"""

import os
import argparse
import re
import numpy as np
import onnxruntime as ort
from pathlib import Path
from transformers import AutoTokenizer

import chromadb
from chromadb import PersistentClient
from chromadb.config import Settings

from pattern_agent import parse_with_agent  # fallback parser


class ONNXMiniLMEmbedder:
    def __init__(self, model_dir="models/all-MiniLM-L6-v2-onnx"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.session = ort.InferenceSession(
            f"{model_dir}/model.onnx",
            providers=["CPUExecutionProvider"]
        )

    def encode(self, texts):
        if isinstance(texts, str):
            texts = [texts]
        tokens = self.tokenizer(texts, padding=True, truncation=True, return_tensors="np")
        inputs = {k: v.astype(np.int64) if v.dtype == np.int32 else v for k, v in tokens.items()}
        ort_outs = self.session.run(None, inputs)
        embeddings = ort_outs[0]  # [batch, seq_len, hidden_size]

        # Mean pooling over tokens
        attention_mask = tokens["attention_mask"]
        masked_embeddings = embeddings * attention_mask[..., None]
        sum_embeddings = masked_embeddings.sum(axis=1)
        lengths = attention_mask.sum(axis=1, keepdims=True)
        sentence_embeddings = sum_embeddings / np.maximum(lengths, 1)

        # L2 normalize
        norms = np.linalg.norm(sentence_embeddings, axis=1, keepdims=True)
        sentence_embeddings = sentence_embeddings / np.maximum(norms, 1e-10)

        return sentence_embeddings


def quick_regex_parse(file_text: str):
    docs = []
    headers = [m for m in re.finditer(r'^\s*#\s*(\d+)\b', file_text, flags=re.MULTILINE)]
    if not headers:
        return docs

    positions = [(m.start(), m.group(1)) for m in headers]
    positions.append((len(file_text), None))

    for i in range(len(positions) - 1):
        start = positions[i][0]
        num = positions[i][1]
        end = positions[i + 1][0]
        block = file_text[start:end]

        desc_match = re.search(r"'''(.*?)'''", block, flags=re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        code_blocks = [m.group(1).strip() for m in re.finditer(r'"""(.*?)"""', block, flags=re.DOTALL)]
        if not code_blocks:
            code_blocks = [m.group(1).strip() for m in re.finditer(r"'''(.*?)'''", block, flags=re.DOTALL)]

        docs.append({
            "id": f"pattern_{num}",
            "description": description,
            "code_blocks": code_blocks or []
        })
    return docs


def make_chroma_client(persist_dir: str):
    os.makedirs(persist_dir, exist_ok=True)
    client = chromadb.PersistentClient(path=persist_dir, settings=Settings(anonymized_telemetry=False))
    return client


def ingest(source_file: str,
           persist_dir: str = "./.chromadb",
           collection_name: str = "patterns",
           reset: bool = False,
           model_dir: str = "models/all-MiniLM-L6-v2-onnx"):

    src_path = Path(source_file)
    if not src_path.exists():
        raise FileNotFoundError(f"{source_file} not found")

    file_text = src_path.read_text(encoding="utf-8")
    parsed = quick_regex_parse(file_text)
    header_count = len(re.findall(r'^\s*#\s*\d+\b', file_text, flags=re.MULTILINE))

    if len(parsed) != header_count:
        print("[ingest] Quick parse incomplete — using agent parser.")
        parsed = parse_with_agent(file_text)
        print(f"[ingest] Agent produced {len(parsed)} patterns.")
    else:
        print(f"[ingest] Quick parsed {len(parsed)} patterns (headers: {header_count}).")

    client = make_chroma_client(persist_dir)

    if reset:
        try:
            client.delete_collection(collection_name)
            print("[ingest] Existing collection deleted (reset).")
        except Exception:
            pass

    col = client.get_or_create_collection(name=collection_name)

    texts, ids, metadatas = [], [], []
    for idx, p in enumerate(parsed):
        base_id = p.get("id") or f"pattern_{idx+1}"
        uniq_id = f"{base_id}_{idx+1}"  # ensure uniqueness
        code_joined = "\n\n---\n\n".join(p.get("code_blocks") or [])
        combined = p.get("description", "").strip()
        if code_joined:
            combined = combined + "\n\n---CODE---\n\n" + code_joined if combined else code_joined
        texts.append(combined or p.get("description") or "")
        ids.append(uniq_id)
        metadatas.append({"source_id": base_id})

    if not texts:
        print("[ingest] No texts found to ingest. Exiting.")
        return

    print("[ingest] Previewing first 3 extracted texts:")
    for i, t in enumerate(texts[:3]):
        print(f"--- Doc {i+1} (len={len(t)} chars) ---")
        print(t[:500])
        print("...")

    print("[ingest] Loading ONNX MiniLM embedder...")
    embed_model = ONNXMiniLMEmbedder(model_dir=model_dir)

    print("[ingest] Computing embeddings...")
    embeddings = embed_model.encode(texts)

    print(f"[ingest] Adding {len(ids)} documents to Chroma collection '{collection_name}'...")
    col.add(documents=texts, embeddings=embeddings.tolist(), ids=ids, metadatas=metadatas)
    print(f"[ingest] Done. Data persisted to: {persist_dir}")

    return col


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="backend/pattern_codeDB.py", help="Path to pattern_codeDB.py (read-only).")
    ap.add_argument("--persist-dir", default="./.chromadb", help="ChromaDB persist directory.")
    ap.add_argument("--collection", default="patterns", help="Collection name.")
    ap.add_argument("--reset", action="store_true", help="Delete existing collection before ingest.")
    ap.add_argument("--model-dir", default="models/all-MiniLM-L6-v2-onnx", help="Path to ONNX MiniLM model dir.")
    args = ap.parse_args()

    ingest(source_file=args.source,
           persist_dir=args.persist_dir,
           collection_name=args.collection,
           reset=args.reset,
           model_dir=args.model_dir)
