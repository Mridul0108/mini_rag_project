
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-120b"


def generate_response(question, retrieved_chunks):

    context = "\n\n".join(
        chunk["chunk"] for chunk in retrieved_chunks
    )

    prompt = f"""
    You are a document-based assistant.

    Answer the question using only the context provided below.
    If the answer is not available in the context, say that you don't know.
    

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_completion_tokens=512
    )

    return response.choices[0].message.content


