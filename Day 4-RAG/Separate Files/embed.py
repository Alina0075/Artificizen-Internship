from qdrant_client.models import PointStruct
from config import model, qdrant_client

def embed_and_store(texts,metadata_list,documents):
    embeddings=model.encode(texts)
    points=[]
    for i in range(len(texts)):
        points.append(
            PointStruct(
                id=i,
                vector=embeddings[i].tolist(),
                payload=metadata_list[i]
            )
        )
    qdrant_client.upsert(
        collection_name=documents, points=points
    )
