from retrival import retrieve
from prompt import build_prompt
from llm import ask

test_cases = [
    {
        "question": "What is AI?",
        "expected": "AI is the simulation of human intelligence."
    },
    {
        "question": "What is Machine Learning?",
        "expected": "Machine Learning is a subset of AI."
    },
    {
        "question": "What is Deep Learning?",
        "expected": "Deep Learning uses neural networks."
    },
    {
        "question": "What is Natural Language Processing?",
        "expected": "NLP enables computers to understand human language."
    },
    {
        "question": "Who is the CEO of Microsoft?",
        "expected": "I don't know."
    }
]
correct = 0

for test in test_cases:

    chunks = retrieve(test["question"], "documents")
    prompt = build_prompt(test["question"], chunks)
    answer = ask(prompt)
    print("\nQuestion:")
    print(test["question"])
    print("\nExpected:")
    print(test["expected"])
    print("\nActual:")
    print(answer)
    score = input("\nScore (C/P/W): ").upper()   
    if score == "C":
        correct += 1

accuracy = (correct / len(test_cases)) * 100

print("\nAccuracy:", accuracy, "%")