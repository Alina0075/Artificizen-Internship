import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_answer(question, chunks, history):

    context = "\n\n".join(
        [
            chunk["text"]
            for chunk in chunks
            if chunk.get("text")
        ]
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are CyberRAG, a cybersecurity evidence assistant.\n\n"

                "STRICT RULES:\n"
                "1. Answer using ONLY the evidence provided in the "
                "Context below.\n"
                "2. Do NOT use outside knowledge.\n"
                "3. Do NOT invent, assume, or hallucinate information.\n"
                "4. If the Context does not contain enough information "
                "to answer the question, reply exactly:\n"
                "I don't know.\n"
                "5. Give a clear and concise answer when the evidence "
                "supports the answer."
            )
        }
    ]

    for chat in history[-6:]:

        role = (
            chat.role.value
            if hasattr(chat.role, "value")
            else chat.role
            if hasattr(chat, "role")
            else chat["role"]
        )

        content = (
            chat.content
            if hasattr(chat, "content")
            else chat["content"]
        )

        if role in ["user", "assistant"]:
            messages.append({
                "role": role,
                "content": content
            })

    messages.append({
        "role": "user",
        "content": (
            f"Context:\n"
            f"{context}\n\n"
            f"Question:\n"
            f"{question}\n\n"
            "Answer only from the Context."
        )
    })

    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content.strip()