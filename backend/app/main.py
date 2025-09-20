import os
from fastapi import FastAPI,Query
from pydantic import BaseModel
from openai import OpenAI
from backend.pattern_retriever import query_patterns

# Create FastAPI app
app = FastAPI(title="PatternGPT - Backend(dev)",version="1.0.0")

# Load OpenRouter API key
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)   

@app.get("/health")
async def health():
    return {"status":"ok","service":"patternGPT","env":"dev"}

@app.get("/")
async def root():
    return {"msg":"patternGPT backend running...  /health for status."}



class AnswerResponse(BaseModel):
    query:str
    best_match:str
    explanation:str
    
    
def call_mistral_model(prompt:str)->str:
    completion = client.chat.completions.create(
        model="mistralai/mistral-small-3.2-24b-instruct:free",
        messages=[
            {"role": "system", "content": "You are a helpful teacher who explains code simply."},
            {"role": "user","content":prompt}
                 ]
    )
    return completion.choices[0].message.content

@app.get("/answer",response_model=AnswerResponse)
async def answer_query(query:str=Query(...,description="Pattern Query"),top_k:int=1):
    hits=query_patterns(query,top_k)
    if not hits["documents"]:
        return AnswerResponse(query=query,best_match="",explanation="Sorry, no pattern found.")
    
    best_doc=hits["documents"][0][0]
    
    prompt =f"""
        User asked: {query}
        
        Returned pattern: {best_doc}
        
        Explain this pattern in natural human language.
        Also provide clear Python code that generates it.
        
        """
        
    explanation=call_mistral_model(prompt)
    
    return AnswerResponse(query=query,best_match=best_doc,explanation=explanation)