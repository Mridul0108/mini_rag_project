
from sentence_transformers import SentenceTransformer
import numpy as np
from app.chunks.document_chunker import chunk_text
from app.loader.document_loader import load_documents
# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")




def generate_embeddings(chunks):
    embeddings = model.encode(chunks)

    return np.array(embeddings)

    
def generate_query_embedding(question):
    embedding = model.encode([question])
    return np.array(embedding[0])

