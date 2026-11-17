from app.loader.document_loader import load_documents

documents=load_documents()

def chunk_text(text, chunk_size=400, overlap=50):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)
        

        start = end - overlap

    return chunks


