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


