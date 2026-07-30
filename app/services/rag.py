import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(question,chunks,history):
    context="\n\n".join([chunk["text"]for chunk in chunks])
    history_text=""
    
    for chat in history:
        history_text+=f"{chat.role}: {chat.content}\n"
        
    prompt=f"""
    You are a cybersecurity assitant.
    Answer ONLY using the provided context.
    If the answer is not present in the context, reply exactly:
    I don't know.
    
    Do not use outside knowledge.
    Do not make up information.
    Conversation History: {history_text}
    Context: {context}
    Question: {question}"""
    
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content