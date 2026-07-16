from dotenv import load_dotenv
from groq import Groq
import os
import time

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)
def ask(prompt,system,model="llama-3.1-8b-instant",temperature=0.7, max_tokens=512):
    messages = []
    if system:
        messages.append({"role":"system", "content":system})
    if prompt:
        messages.append({"role":"user","content":prompt})
    
    response=client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )    
    return response

prompt="What is Machine Learning?"
system="You are a strict JSON-only responder. Never output anything outside a JSON object."

models={"llama-3.3-70b-versatile", "Llama-3.1-8b-instant"}
for model in models:
    start=time.time()
    response=ask(prompt,system,model=model)
    end=time.time()
    print("Model:", model)
    print(response.choices[0].message.content)
    print("\nPrompt Tokens:", response.usage.prompt_tokens)
    print("Completion Tokens:", response.usage.completion_tokens)
    print("Total Tokens:", response.usage.total_tokens)
    print(f"Latency: {end - start:.2f} seconds\n")
    
    
