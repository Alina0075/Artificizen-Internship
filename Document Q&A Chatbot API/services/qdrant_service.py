from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)
import uuid

collection_name="documents"
client = QdrantClient(path="qdrant_db")
collections= client.get_collections().collections
collection_names=[collection.name for collection in collections]

if collection_name not in collection_names:
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )

def store_chunks(chunks,embeddings,filename):
    """Store the chunks and their embeddings in Qdrant"""
    points=[]
    for i,(chunk,embedding) in enumerate(zip(chunks,embeddings)):
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "text":chunk,
                    "filename":filename,
                    "chunk_index":i
                }
            )
        )
    client.upsert(
        collection_name=collection_name,
        points=points
    )

def search_chunks(query_embedding, limit=3):
    """Search for the most similar chunks"""

    response = client.query_points(
        collection_name=collection_name,
        query=query_embedding,
        limit=limit,
    )

    retrieved_chunks = []

    for point in response.points:
        retrieved_chunks.append(
            {
                "text": point.payload.get("text", ""),
                "filename": point.payload.get("filename", ""),
                "chunk_index": point.payload.get("chunk_index", 0),
                "score": point.score,
            }
        )

    return retrieved_chunks

