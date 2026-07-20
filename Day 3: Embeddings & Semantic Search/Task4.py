from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient

from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue
)

model = SentenceTransformer("all-MiniLM-L6-v2")
client=QdrantClient(":memory:") #everything stays in the RAM and when program ends everything is deleted
client.create_collection(
    collection_name="articles",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

documents = [
    "Dogs love to play fetch in the park.",
    "Cats enjoy sleeping on warm sofas.",
    "Python is a popular programming language used for AI.",
    "Artificial Intelligence is transforming healthcare and education.",
    "Machine Learning is a subset of Artificial Intelligence.",
    "Pizza is one of the most popular foods worldwide.",
    "Basketball is played by two teams of five players.",
    "The Earth revolves around the Sun once every year.",
    "Cloud computing provides scalable computing resources.",
    "Neural networks are inspired by the human brain."
]

embeddings=model.encode(documents)
points=[]
for i in range(len(documents)):
    points.append(
        PointStruct(
            id=i,
            vector=embeddings[i].tolist(),
            payload={"source":"manual" if i % 2 == 0 else "blog","document":documents[i]}
        )
    )
    client.upsert(
        collection_name="articles",points=points)

query = "How is AI used in medicine?"

query_embedding = model.encode(query)

results=client.query_points(
    collection_name="articles",
    query=query_embedding.tolist(),
    query_filter=Filter(must=[FieldCondition(key="source",match=MatchValue(value="manual"))]),
    limit=2).points

for i in results:
    print(i.payload["document"])
    print(i.score)
    print(i.payload["source"])
    print()