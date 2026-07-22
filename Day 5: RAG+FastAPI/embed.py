from qdrant_client.models import PointStruct
from config import model, qdrant_client

def embed_and_store(texts, metadata_list, documents):

    print("embed_and_store() called")
    print("Number of texts:", len(texts))
    print("Number of metadata:", len(metadata_list))

    embeddings = model.encode(texts)

    print("Embeddings:", len(embeddings))

    points = []

    for i in range(len(texts)):
        points.append(
            PointStruct(
                id=i,
                vector=embeddings[i].tolist(),
                payload=metadata_list[i]
            )
        )

    print("Points:", len(points))

    qdrant_client.upsert(
        collection_name=documents,
        points=points
    )

    print("Upsert finished")

    print(qdrant_client.count(collection_name=documents))