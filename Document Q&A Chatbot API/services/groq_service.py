import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not found in .env file.")

client= Groq(api_key=api_key)
def generate_answer(context:str, query:str,history):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a RAG assistant.\n\n"
                "Answer ONLY using the provided context.\n"
                "If the answer is not found in the context,\n"
                'reply exactly: "I don\'t know."'
            )
        }
    ]
    messages.extend(history)
    messages.append(
        {
            "role":"user",
            "content":f"""
Context:{context}
Question: {query}
            """
            
        }
    )
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content.strip()
def stream_answer(context,query,history):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a RAG assistant.\n"
                "Answer ONLY using the provided context.\n"
                "If the answer is not present in the context, "
                "reply exactly: I don't know."
            )
        }
    ]
    messages.extend(history)
    messages.append(
        {
            "role": "user",
            "content": f"""
                Context: {context}
                Question: {query}
            """
        }
    )
    stream=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0,
        stream=True
    )
    for chunk in stream:

        if chunk.choices:

            delta = chunk.choices[0].delta.content

            if delta is not None:
                yield delta
                