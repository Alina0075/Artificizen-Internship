from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

collection_name="cyber_rag"
client=QdrantClient(path="qdrant_storage")
if collection_name not in client.get_collections().collections:
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384,distance=Distance.COSINE)
    )
    

