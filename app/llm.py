
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-120b"


def generate_response(question, retrieved_chunks, conversation_history):

    context = "\n\n".join(
        chunk["chunk"] for chunk in retrieved_chunks
    )

    messages = [
        {
            "role": "system",
            "content": f"""
            You are a document-based assistant.

            Answer the question using only the provided document context.
            If the answer is not available in the context,
            say that you don't know.

            Use conversation history to understand follow-up questions,
            but do not treat previous assistant answers as factual evidence.

            Context:
            {context}
            """
        }
    ]

    
    messages.extend(conversation_history)

    
    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.3,
        max_completion_tokens=512
    )

    return response.choices[0].message.content
