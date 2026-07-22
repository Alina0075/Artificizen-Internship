from config import model, qdrant_client
def retrieve(query,collection,top_k=3):
    query_embedding=model.encode(query).tolist()
    results=qdrant_client.query_points(
        collection_name=collection,
        query=query_embedding,
        limit=top_k
    )
    chunks=[]
    for point in results.points:
        chunks.append(point.payload["text"])
    return chunks

def retrieve_with_metadata(query, collection, top_k=3):

    query_embedding = model.encode(query).tolist()

    results = qdrant_client.query_points(
        collection_name=collection,
        query=query_embedding,
        limit=top_k
    )

    return results.points