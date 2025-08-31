from fastapi import FastAPI
import fastapi
from pydantic import BaseModel

app = FastAPI(title="PatternGPT - Backend(dev)")

@app.get("/health")
async def health():
    return {"status":"ok","service":"patternGPT","env":"dev"}

@app.get("/")
async def root():
    return {"msg":"patternGPT backend running...  /health for status."}