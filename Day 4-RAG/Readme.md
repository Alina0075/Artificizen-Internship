# Retrieval-Augmented Generation (RAG) Pipeline

A simple end-to-end **Retrieval-Augmented Generation (RAG)** application built in Python using **Sentence Transformers**, **Qdrant**, and **Groq's Llama 3.3 70B Versatile** model.

This project demonstrates how to load documents, split them into chunks, generate embeddings, store them in a vector database, retrieve relevant information, and generate grounded responses using an LLM.

---

## Features

- Load a text document
- Split documents into overlapping chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in Qdrant
- Perform semantic similarity search
- Build prompts using retrieved context
- Generate responses with Groq Llama 3.3 70B Versatile
- Compare responses with and without RAG

---

## Technologies Used

- Python 3
- Sentence Transformers
- Qdrant Vector Database
- Groq API
- python-dotenv

---

## Project Structure

```
Day 4/
│
├── main.py
├── document.txt
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-pipeline.git
cd rag-pipeline
```

---

### 2. Create a virtual environment

Windows

```bash
python -m venv ai_venv
```

Activate

```bash
ai_venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a **.env** file in the project directory.

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## Running the Project

Run

```bash
python main.py
```

---

## RAG Pipeline

```
Document
   │
   ▼
Load Text
   │
   ▼
Chunk Text
   │
   ▼
Generate Embeddings
   │
   ▼
Store in Qdrant
   │
────────────────────────────
User Question
   │
   ▼
Generate Query Embedding
   │
   ▼
Retrieve Similar Chunks
   │
   ▼
Build Prompt
   │
   ▼
Groq Llama 3.3 70B
   │
   ▼
Generated Answer
```

---

## Implemented Functions

### chunk_text()

Splits long documents into overlapping chunks.

**Parameters**

- text
- chunk_size (default = 500)
- overlap (default = 50)

Returns

- List of chunks

---

### embed_and_store()

Generates embeddings for each chunk and stores them inside Qdrant.

Metadata stored:

- Source filename
- Chunk index
- Original text

---

### retrieve()

Embeds the user's query and retrieves the most relevant chunks from Qdrant.

Returns

- Top-k relevant chunks

---

### build_prompt()

Builds the prompt by inserting retrieved chunks before the user's question.

Prompt format:

```
Context:
1. ...
2. ...
3. ...

Question:
...

Answer using only the context above.
If the answer is not in the context, say:
I don't know.
```

---

### ask()

Sends the augmented prompt to Groq using the **llama-3.3-70b-versatile** model and returns the generated response.

---

## Example Questions

```
What is Retrieval-Augmented Generation?

Why is overlap important during chunking?

Who is the CEO of Microsoft?
```

Expected behavior:

- Questions found in the document are answered correctly.
- Questions not covered by the document return:

```
I don't know.
```

---

## Hallucination Test

The project compares:

### Without RAG

- The LLM answers using only its pre-trained knowledge.

### With RAG

- Relevant document chunks are retrieved first.
- The LLM answers only from the retrieved context.
- Hallucinations are significantly reduced.

---

## Learning Outcomes

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Text Chunking
- Sentence Embeddings
- Vector Databases
- Prompt Engineering
- Grounded Response Generation
- Groq API Integration

---

## Dependencies

- sentence-transformers
- qdrant-client
- groq
- python-dotenv
- torch


Artificizen (Pvt.) Ltd.

---
