from app.services.qdrant_db import client, collection_name
from app.services.embedder import get_embedding

from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)


def search_documents(room_id: int, query: str):

    vector = get_embedding(query)


    results = client.query_points(
        collection_name=collection_name,
        query=vector,
        limit=5,
        query_filter=Filter(
            must=[
                FieldCondition(
                    key="room_id",
                    match=MatchValue(value=room_id)
                )
            ]
        ),
        with_payload=True
    )
    return [
        point.payload
        for point in results.points
        if point.payload
    ]