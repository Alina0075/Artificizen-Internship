from app.services.qdrant_db import client

def search_documents(vector,room_id):
    results=client.search(
        collection_name="cyber_rag",
        query_vector=vector,
        limit=5,
        query_filter={
            "must":[
                {
                    "key":"room_id",
                    "match":{
                        "value":room_id
                    }
                }
            ]
        }
    )
    return results