"""
Pattern Retriever
-----------------
This script queries the 'patterns' collection in ChromaDB
using ONNX MiniLM embeddings for semantic search.

Steps:
1. Load tokenizer and ONNX model.
2. Encode query into an embedding (same pooling as in ingestion).
3. Search top-k nearest patterns from ChromaDB.
4. Print results with metadata and preview.

"""


import argparse
import numpy as np
import onnxruntime as ort
from transformers import AutoTokenizer
import chromadb


class OnnxEmbedder:
    def __init__(self,model_dir="models/all-MiniLM-L6-v2-onnx"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.session=ort.InferenceSession(
            f"{model_dir}/model.onnx",providers=["CPUExecutionProvider"]
        )
        
    def encode(self,texts):
        """Convert a list of texts into sentence embeddings."""
        tokens=self.tokenizer(texts,padding=True,truncation=True,return_tensors="np")
        inputs={k: v.astype(np.int64) if v.dtype==np.int32 else v for k,v in tokens.items()}
        ort_outs=self.session.run(None,inputs)
        embeddings=ort_outs[0]
        
    #Mean pooling
        attention_mask=tokens["attention_mask"]
        masked_embeddings=embeddings*attention_mask[...,None]
        sum_embeddings=masked_embeddings.sum(axis=1)
        lengths=attention_mask.sum(axis=1,keepdims=True)
        sentence_embeddings=sum_embeddings/np.maximum(lengths,1)
        
        # Normalize
        norms = np.linalg.norm(sentence_embeddings, axis=1, keepdims=True)
        return sentence_embeddings / np.maximum(norms, 1e-10)
        
def query_patterns(query,top_k=3,db_path="./.chromadb"):
    embedder=OnnxEmbedder()
    query_emb=embedder.encode([query])[0]
    client=chromadb.PersistentClient(path=db_path)
    col=client.get_collection("patterns")
    results=col.query(query_embeddings=[query_emb.tolist()],n_results=top_k)
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help="Search query text")
    parser.add_argument("--top_k", type=int, default=3, help="Number of results to retrieve")
    args = parser.parse_args()

    hits = query_patterns(args.query, args.top_k)

    print(f"\nTop {args.top_k} results for query: '{args.query}'\n")
    for i in range(len(hits["documents"][0])):
        print(f"Result {i+1}:")
        print("Metadata:", hits["metadatas"][0][i])
        print("Text preview:", hits["documents"][0][i][:300])
        print("-" * 40)

