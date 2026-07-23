import hashlib
query_cache={}
def get_cache_key(session_id:str,query:str):
    query_hash=hashlib.sha256(query.encode('utf-8')).hexdigest()
    return f"{session_id}:{query_hash}"

def get_cached_answer(session_id:str,query:str):
    cache_key=get_cache_key(session_id,query)
    return query_cache.get(cache_key)

def save_cached_answer(session_id:str,query:str,answer:str,sources):
    cache_key=get_cache_key(session_id,query)
    query_cache[cache_key]={
        "answer":answer,
        "sources":sources
    }