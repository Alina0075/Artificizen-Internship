from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences=[
    "Dog is chasing a ball.",
    "I like Cats.",
    "Fries are good.",
    "Artiificial Intelligence is the future.",
    "The weather is nice today.",
    "Its raining outside.",
    "A puppy is running after the ball."
]

embeddings=model.encode(sentences)
print(embeddings.shape)

def cosine_similarity(vec1, vec2):
    dot_product=np.dot(vec1,vec2)
    magnitude1=np.linalg.norm(vec1)
    magnitude2=np.linalg.norm(vec2)
    if magnitude1==0 or magnitude2==0:
        return 0
    else:
        return dot_product/(magnitude1*magnitude2)
    
results=[]
for i in range(len(sentences)):
    for j in range(i+1,len(sentences)):
        similarity=cosine_similarity(embeddings[i],embeddings[j])
        results.append((sentences[i], sentences[j], similarity))

results.sort(key=lambda x:x[2],reverse=True)
print("Ranked Similarity Results:")

for sentence1, sentence2, similarity in results:
    print(f"Sentence 1: {sentence1}")
    print(f"Sentence 2: {sentence2}")
    print(f"Cosine Similarity: {similarity:.4f}")


