from retrival import retrieve
from prompt import build_prompt
from llm import ask

test_cases = [
    {
        "question": "What is Artificial Intelligence?",
        "ground_truth": "Artificial Intelligence is the simulation of human intelligence."
    },
    {
        "question": "What are the capabilities of AI systems?",
        "ground_truth": "AI systems can perceive, reason, learn and take autonomous actions."
    },
    {
        "question": "What is Machine Learning?",
        "ground_truth": "Machine Learning is a subset of AI."
    },
    {
        "question": "What is Deep Learning?",
        "ground_truth": "Deep Learning uses neural networks."
    },
    {
        "question": "Who is the CEO of Microsoft?",
        "ground_truth": "I don't know."
    }
]

faithfulness_scores = []
relevancy_scores = []

lowest_score = 100
lowest_question = ""

for test in test_cases:

    chunks = retrieve(test["question"], "documents")
    prompt = build_prompt(test["question"], chunks)
    answer = ask(prompt)

    context = "\n".join(chunks)
    faithfulness_prompt = f"""
You are evaluating a RAG system.

Context:
{context}

Answer:
{answer}

Give ONLY a score from 0 to 100 indicating how well the answer is supported by the context.

Output only the number.
"""

    faithfulness = ask(faithfulness_prompt)

    relevancy_prompt = f"""
Question:
{test["question"]}

Answer:
{answer}

Give ONLY a score from 0 to 100 indicating how relevant the answer is to the question.

Output only the number.
"""

    relevancy = ask(relevancy_prompt)

    try:
        faithfulness = float(faithfulness.strip())
    except:
        faithfulness = 0

    try:
        relevancy = float(relevancy.strip())
    except:
        relevancy = 0

    faithfulness_scores.append(faithfulness)
    relevancy_scores.append(relevancy)

    average = (faithfulness + relevancy) / 2

    if average < lowest_score:
        lowest_score = average
        lowest_question = test["question"]

    print("=" * 60)
    print("Question:", test["question"])
    print("Answer:", answer)
    print("Faithfulness:", faithfulness)
    print("Answer Relevancy:", relevancy)

print("\n" + "=" * 60)

print("Average Faithfulness:",
      sum(faithfulness_scores) / len(faithfulness_scores))

print("Average Answer Relevancy:",
      sum(relevancy_scores) / len(relevancy_scores))

print("\nLowest Scoring Question:")
print(lowest_question)

print("\nReason:")
print("The generated answer was either not fully supported by the retrieved context or was less relevant to the user's question.")