import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from numpy import full
from fastapi import FastAPI,Query
from pydantic import BaseModel
from openai import OpenAI
from backend.pattern_retriever import query_patterns
from typing import List,Dict
from backend.pattern_answerer import answer_query   

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


class ChatMessage(BaseModel):
    role:str
    content:str
    
class ChatRequest(BaseModel):
    history:List[ChatMessage]
    query:str
    
class ChatResponse(BaseModel):
    reply:str
    code:str
    
@app.post("/chat",response_model=ChatResponse)
async def chat(req:ChatRequest):
    
    explanation = await answer_query(req.query, top_k=1)
    explanation = str(explanation)


    # Step 2: Extract code block if present
    code = ""
    if "```" in explanation:
        parts = explanation.split("```")
        explanation = parts[0].strip()
        code = parts[1].replace("python", "").strip()

    return ChatResponse(reply=explanation, code=code)
    
    """  hits=query_patterns(req.query,top_k=1)
    best_doc=hits["documents"][0][0] if hits["documents"] else ""
    
    messages=[{"role":m.role,"content":m.content} for m in req.history]
    messages.append({"role":"user","content":f"{req.query}\n\nBest pattern match: {best_doc }"})
    
    completion=client.chat.completions.create(
        model="mistralai/mistral-small-3.2-24b-instruct:free",
        messages=[{"role": "system", "content": "You are a helpful assistant that explains coding patterns clearly."}] + messages
    )
    
    full_reply = completion.choices[0].message.content

    # Always coerce to string
    if isinstance(full_reply, list):
        full_reply = " ".join(str(x) for x in full_reply)
    else:
        full_reply = str(full_reply)
 
        
    if "```" in full_reply:
        parts = full_reply.split("```")
        explanation = parts[0].strip()   # ✅ keep as string
        code = parts[1].replace("python", "").strip()
    else:
        explanation = full_reply
        code = ""

        
    return ChatResponse(reply=explanation,code=code)
    
     """
     
     