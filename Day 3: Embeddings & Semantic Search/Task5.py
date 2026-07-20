from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
documents = [
    "The child is riding a bicycle.",
    "Dogs love playing fetch.",
    "Cats sleep on sofas.",
    "Python is a programming language.",
    "Artificial Intelligence is changing healthcare.",
    "Machine Learning uses data.",
    "The sun rises in the east.",
    "Pizza tastes delicious.",
    "Football is played worldwide.",
    "Cloud computing is scalable.",
    "Books improve knowledge.",
    "Birds can fly.",
    "The car needs fuel.",
    "Trees produce oxygen.",
    "Water freezes at zero degrees.",
    "Students study for exams.",
    "Teachers explain lessons.",
    "Hospitals treat patients.",
    "Doctors prescribe medicine.",
    "Music helps people relax.",
    "Coffee contains caffeine.",
    "The internet connects computers.",
    "Mountains are very tall.",
    "Fish live underwater.",
    "The moon orbits Earth.",
    "Computers process information.",
    "Basketball uses a hoop.",
    "A smartphone has many apps.",
    "Exercise improves health.",
    "Reading develops vocabulary.",
    "Programming requires logical thinking.",
    "Neural networks recognize patterns.",
    "Birds build nests.",
    "Cars have engines.",
    "Rain helps plants grow.",
    "The chef prepared dinner.",
    "The baby is sleeping.",
    "A lion is a wild animal.",
    "Elephants have long trunks.",
    "The artist painted a portrait.",
    "The train arrived on time.",
    "The farmer harvested wheat.",
    "The pilot flew the airplane.",
    "The student solved the math problem.",
    "The baby laughed happily.",
    "A rabbit eats carrots.",
    "The gardener watered the flowers.",
    "The programmer fixed the bug.",
    "The child is reading a storybook.",
    "The astronaut explored space."
]
embeddings=model.encode(documents)
def cosine_similarity(vec1,vec2):
    return np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))

query="How is AI used in medicine?"
query_embedding=model.encode(query)
results=[]
for i in range(len(documents)):
    similarity=cosine_similarity(query_embedding,embeddings[i])
    results.append((documents[i],similarity))
    
results.sort(key=lambda x:x[1],reverse=True)
print("Top 3 Similar Documents:")
for document, similarity in results[:3]:
    print(f"Document: {document}")
    print(f"Cosine Similarity: {similarity:.4f}")
    print()