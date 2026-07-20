import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client=chromadb.Client()
collection=client.create_collection("similarity")

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

ids = [
    "1","2","3","4","5",
    "6","7","8","9","10"
]
embeddings=model.encode(documents)
collection.add(ids=ids, documents=documents, embeddings=embeddings.tolist() )
query = "How is AI used in medicine?"
query_embedding = model.encode(query)
results=collection.query(query_embeddings=query_embedding, n_results=2)
print("Top 2 Similar Documents:")
for document, similarity in zip(results['documents'][0], results['distances'][0]):
    print(f"Document: {document}")
    print(f"Cosine Similarity: {similarity:.4f}")
    print()



