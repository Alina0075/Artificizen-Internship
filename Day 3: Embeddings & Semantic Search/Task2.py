from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents=[
    "Dog is chasing a ball.",
    "I like Cats.",
    "Fries are good.",
    "Artiificial Intelligence is the future.",
    "The weather is nice today.",
    "Its raining outside.",
    "A puppy is running after the ball."
]

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    
def semantic_search(query,documents):
    query_embedding=model.encode(query)
    document_embeddings=model.encode(documents)
    result=[]
    for i in range(len(documents)):
        similarity=cosine_similarity(query_embedding,document_embeddings[i])
        result.append((documents[i],similarity))
    
    result.sort(key=lambda x:x[1],reverse=True)
    return result

query="The weather is cool today."
top_results=semantic_search(query,documents)
print("Top 3 Similar Documents:")
for document, similarity in top_results[:3]:
    print(f"Document: {document}")
    print(f"Cosine Similarity: {similarity:.4f}")
    print()