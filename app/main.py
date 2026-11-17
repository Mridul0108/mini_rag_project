
from app.loader.document_loader import load_documents
from app.chunks.document_chunker import chunk_text
from app.embeddings.document_embed import (
    generate_embeddings,
    generate_query_embedding
    )
from app.retriever.document_retriever import retrieve_chunks
from app.llm import generate_response



documents = load_documents()

print(f"Loaded {len(documents)} documents")


all_chunks = []

for document in documents:
    document_chunks = chunk_text(document["content"])
    all_chunks.extend(document_chunks)

print(f"Generated {len(all_chunks)} chunks")



embeddings = generate_embeddings(all_chunks)

print("Document embeddings generated successfully")



def ask_question(question):


    query_embedding = generate_query_embedding(question)


    retrieved_chunks = retrieve_chunks(
        query_embedding,
        embeddings,
        all_chunks,
        top_k=3
    )

 
    answer = generate_response(
        question,
        retrieved_chunks
    )

    return answer


# Step 5: Run the chatbot
if __name__ == "__main__":

    while True:
        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            print("Chatbot stopped.")
            break

        answer = ask_question(question)

        print("\nAssistant:", answer)
