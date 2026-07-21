from chunk import chunk_texts
from embed import embed_and_store
from retrival import retrieve
from prompt import build_prompt
from llm import ask


with open("document.txt", "r", encoding="utf-8") as f:
    document = f.read()

chunks = chunk_texts(document)

metadata = []

for i, chunk in enumerate(chunks):
    metadata.append({
        "source": "document.txt",
        "chunk_index": i,
        "text": chunk
    })

embed_and_store(chunks, metadata, "documents")

questions = [
    "What is RAG?",
    "Why is overlap important?",
    "Who is the CEO of Microsoft?"
]

for question in questions:

    retrieved = retrieve(question, "documents")

    prompt = build_prompt(question, retrieved)

    answer = ask(prompt)

    print("=" * 50)
    print("Question:", question)
    print("Answer:", answer)