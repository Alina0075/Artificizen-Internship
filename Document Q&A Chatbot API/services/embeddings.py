from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(texts:str)->list:
    """
    Convert a piece of text in to embedding vector
    
    """
    embeddings = embedding_model.encode(texts)
    return embeddings    
