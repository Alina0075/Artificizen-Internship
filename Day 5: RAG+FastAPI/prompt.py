def build_prompt(query, chunks):

    context = ""

    for i, chunk in enumerate(chunks):
        context += f"{i+1}. {chunk}\n\n"

    return f"""
Context:

{context}

Question:
{query}

Answer using only the context above.

If the answer is not in the context, say:
I don't know.
"""