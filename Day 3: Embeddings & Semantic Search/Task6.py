from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient

from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

model = SentenceTransformer("all-MiniLM-L6-v2")
client=QdrantClient(":memory:")
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

def embed_and_store(texts,metadata_list,collection):
    embeddings = model.encode(texts)
    points=[]
    for i in range(len(texts)):
        points.append(
            PointStruct(
                id=i,
                vector=embeddings[i].tolist(),
                payload=metadata_list[i]
            )
        )
    client.upsert(
        collection_name=collection,points=points)
    print("Documents stored successfully!")

texts = [
    "Python is a programming language.",
    "Artificial Intelligence is transforming healthcare.",
    "Dogs love playing fetch."
]

metadata = [
    {
        "source":"manual",
        "category":"Programming"
    },
    {
        "source":"manual",
        "category":"AI"
    },
    {
        "source":"blog",
        "category":"Pets"
    }
]
embed_and_store(texts,metadata,"documents")
