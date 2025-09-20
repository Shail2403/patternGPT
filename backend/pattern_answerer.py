"""
Pattern Answerer using Mistral-7B-Instruct free via OpenRouter
-------------------------------------------------------------
Retrieves patterns and generates human-readable explanations with code.
"""

import argparse
from openai import OpenAI
from pattern_retriever import query_patterns

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def call_mistral_model(prompt: str) -> str:
    """Send prompt to Mistral-7B-Instruct and return text response."""
    completion = client.chat.completions.create(
        model="mistralai/mistral-small-3.2-24b-instruct:free",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

def answer_query(query: str, top_k: int = 1):
    # Step 1: Retrieve top-k patterns
    hits = query_patterns(query, top_k)
    if not hits["documents"]:
        return "Sorry, no matching pattern found."

    best_doc = hits["documents"][0][0]

    # Step 2: Prepare prompt for the model
    prompt = f"""
User asked: {query}

Retrieved pattern:
{best_doc}

Explain this pattern in simple, human-friendly language
and include working Python code.
"""
    # Step 3: Call Mistral model
    explanation = call_mistral_model(prompt)
    return explanation

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help="Search query text")
    parser.add_argument("--top_k", type=int, default=1, help="Number of results to retrieve")
    args = parser.parse_args()

    final_answer = answer_query(args.query, args.top_k)
    print("\n=== Final Answer ===\n")
    print(final_answer)
