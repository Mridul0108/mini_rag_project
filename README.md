# Mini RAG Chatbot

## About the Project

This is a simple RAG (Retrieval-Augmented Generation) chatbot built using Python. The main purpose of this project is to understand how RAG works internally without using frameworks like LangChain or LlamaIndex.

The chatbot reads documents, splits their content into smaller chunks, generates embeddings, and retrieves relevant information based on the user's question. It then uses the Groq API to generate an answer from the retrieved content.

## Technologies Used

- Python
- Sentence Transformers
- NumPy
- Scikit-learn
- PyPDF
- python-docx
- Groq API
- Python dotenv

## Project Structure

```text
mini_rag_chatbot/
│
├── app/
│   ├── loader/
│   │   └── document_loader.py
│   │
│   ├── chunks/
│   │   └── document_chunker.py
│   │
│   ├── embeddings/
│   │   └── document_embed.py
│   │
│   ├── retriever/
│   │   └── retriever.py
│   │
│   ├── llm.py
│   │
│   ├── memory/
│   │   └── conversation_memory.py
│   │
│   └── main.py
│
├── docs/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

The project is divided into different parts:

1. **Document Loading:** Reads PDF and DOCX files from the docs folder and extracts their text.

2. **Text Chunking:** Splits the extracted text into smaller chunks of around 400 characters with some overlap.

3. **Embedding Generation:** Uses the Sentence Transformer model `all-MiniLM-L6-v2` to convert document chunks into numerical vectors.

4. **Retrieval:** Converts the user's question into an embedding and compares it with document embeddings using cosine similarity. It retrieves the top 3 matching chunks.

5. **Answer Generation:** Sends the retrieved chunks and user's question to the Groq API. The LLM generates an answer using the provided document context.

6. **Conversation Memory:** Stores user messages and assistant responses in a Python list. It keeps the latest 20 messages and includes previous messages when generating a response.

## Setup and Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd mini_rag_chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Add documents

Place your PDF or DOCX files inside the `docs/` folder.

### 6. Run the project

```bash
python -m app.main
```

You can now ask questions about the documents.

Type `exit` or `quit` to stop the chatbot.

## Current Features

- Supports PDF and DOCX documents.
- Splits documents into smaller text chunks.
- Generates embeddings using Sentence Transformers.
- Retrieves relevant chunks using cosine similarity.
- Generates answers using Groq API.
- Maintains conversation history using Python lists.
- Keeps the latest 20 messages in memory.

## Future Improvements

- Store conversation history in SQLite using SQLAlchemy.
- Load previous conversation history after restarting the application.
- Improve document source tracking and retrieval.

