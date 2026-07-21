from sentence_transformers import SentenceTransformer
from groq import Groq
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=api_key)
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

model=SentenceTransformer("all-MiniLM-L6-v2")
client=QdrantClient(":memory:")
client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

def embed_and_store(texts,metadata_list,documents):
    embeddings=model.encode(texts)
    points=[]
    for i in range(len(texts)):
        points.append(
            PointStruct(
                id=i,
                vector=embeddings[i].tolist(),
                payload=metadata_list[i]
            )
        )
    client.upsert(
        collection_name=documents, points=points
    )

#1.	Write a chunk_text(text, chunk_size=500, overlap=50) function that splits a long string into overlapping chunks
def chunk_texts(texts,chunk_size=500, overlap=50):
    chunks=[]
    start=0
    while start<len(texts):
        end=start+chunk_size
        chunk=texts[start:end]
        if chunk:
            chunks.append(chunk)
        start+=chunk_size-overlap
    return chunks



with open("document.txt","r",encoding="utf-8") as f:
    document=f.read()
    
chunks=chunk_texts(document)
print(f"Total chunks created: {len(chunks)}")

#2.	Store the chunks in Qdrant with metadata that includes the source document name and the chunk index.
metadata=[]
for i,chunk in enumerate(chunks):
    metadata.append(
        {
            "source":"document.txt",
            "chunk_index":i,
            "text":chunk
        }
    )
    
embed_and_store(chunks,metadata,"documents")
print(f"Stored {len(chunks)} chunks in Qdrant successfully.")


#3.	Write a retrieve(query, collection, top_k=3) function that embeds the query with sentence-transformers and returns the top-k chunks from Qdrant.
def retrieve(query,collection,top_k=3):
    query_embedding=model.encode(query).tolist()
    results=client.query_points(
        collection_name=collection,
        query=query_embedding,
        limit=top_k
    )
    chunks=[]
    for point in results.points:
        chunks.append(point.payload["text"])
    return chunks

query="What is the impact of AI in healthcare?"
top_chunks=retrieve(query,"documents")
print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(top_chunks):
    print(f"Chunk {i+1}:")
    print(chunk)
    
#4.	Write a build_prompt(query, chunks) function that inserts the retrieved chunks as numbered context items and appends: “Answer using only the context above. If the answer is not in the context, say: I don’t know.”
def build_prompt(query, chunks):
    context=""
    for i, chunk in enumerate(chunks):
        context+=f"{i+1}.{chunk}\n\n"
    prompt=f"""
context:{context}
Question:{query}
Answer using only the context above.

If the answer is not in the context, say:
I don't know.
"""
    return prompt

prompt=build_prompt(query,top_chunks)
print("\nGenerated Prompt:\n")
print(prompt)

#5.	Wire everything together: retrieve() → build_prompt() → ask() (using Groq). Ask three questions — two with answers in the document and one without. Verify the model says “I don’t know” for the third.
def ask(prompt):
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content
questions = [
    "What is RAG?",
    "Why is overlap important in chunking?",
    "Who is the CEO of Microsoft?"
]
for question in questions:
    chunks=retrieve(question,"documents")
    prompt=build_prompt(question,chunks)
    answer=ask(prompt)
    print(f"\nQuestion: {question}")
    print(f"Answer: {answer}")


#6.	Test hallucination: run the same question WITHOUT the RAG context (raw Groq call only). Compare the answer to the RAG answer. Write a short observation on which is more grounded and why.
question = "Who is the CEO of Microsoft?"

response = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

print("Without RAG:")
print(f"Question: {question}")
print(response.choices[0].message.content)

chunks = retrieve(question, "documents")

prompt = build_prompt(question, chunks)

answer = ask(prompt)

print("\nWith RAG:")
print(f"Question: {question}")
print(answer)