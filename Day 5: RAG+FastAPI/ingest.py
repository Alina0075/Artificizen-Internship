from chunk import chunk_texts
from embed import embed_and_store

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
