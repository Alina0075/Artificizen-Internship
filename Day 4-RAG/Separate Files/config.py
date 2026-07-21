import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

model = SentenceTransformer("all-MiniLM-L6-v2")

groq_client = Groq(api_key=api_key)

qdrant_client = QdrantClient(":memory:")

qdrant_client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)