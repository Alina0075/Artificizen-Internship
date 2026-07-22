from retrival import retrieve
from prompt import build_prompt
from llm import stream_answer
from cache import cache, get_cache_key
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from retrival import retrieve, retrieve_with_metadata
from history import chat_history, add_to_history

app=FastAPI()
class QueryRequest(BaseModel):
    query: str

@app.post("/chat")
def chat(request: QueryRequest):
    query_hash=get_cache_key(request.query)    
    if query_hash in cache:
        print("Cache hit")
    else:
        print("Cache miss")
    chunks=retrieve(request.query,"documents")
    prompt=build_prompt(request.query,chunks,)
    messages=[]
    messages.extend(chat_history)
    messages.append({"role":"user","content":prompt})
    return StreamingResponse(
        stream_answer(messages),
        media_type="text/plain"
    )



"""
    add_to_history("user",request.query)
    add_to_history("assistant",answer)
    metadata=retrieve_with_metadata(request.query,"documents")
    sources=[]
    for point in metadata:
        sources.append({"source":point.payload["source"],"chunk_index":point.payload["chunk_index"]})
    response = {"answer":answer,"sources":sources}
    cache[query_hash] = response
    return response
"""    
    
    