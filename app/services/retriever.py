from app.services.qdrant_db import client
from app.services.embedder import model
from qdrant_client.models import Filter, FieldCondition, MatchValue

def search_documents(room_id:int,query:str):
    vector=model.encode(query).tolist()
    
    results=client.query_points(
        collection_name="cyber_rag",
        query=vector,
        limit=5,
        query_filter=Filter(
            must=[
                FieldCondition(
                    key="room_id",
                    match=MatchValue(value=room_id)
                )
            ]
        )
    )
    for point in results.points:
        print(
            "FILE:", point.payload["filename"],
            "| FILE ID:", point.payload["file_id"],
            "| CHUNK:", point.payload["chunk_index"],
            "| SCORE:", point.score
        )
    return [point.payload for point in results.points]