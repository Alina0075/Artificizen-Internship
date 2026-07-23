# 📄 Document Q&A Chatbot API (RAG)

A Retrieval-Augmented Generation (RAG) chatbot built with **FastAPI**, **Groq**, **Sentence Transformers**, and **Qdrant**.

The chatbot allows users to upload documents (TXT/PDF), indexes them into a vector database, and answers questions using only the uploaded document.

---

## Features

- Upload TXT and PDF documents
- Automatic document chunking
- Local embeddings using Sentence Transformers
- Vector storage using Qdrant
- Semantic search (Top-3 retrieval)
- Grounded answers using Groq Llama 3.3
- Returns document sources
- Multi-turn conversation history
- Query cache
- Streaming responses
- Pytest test suite

---

## Tech Stack

- Python 3.13+
- FastAPI
- Groq API
- Sentence Transformers
- Qdrant
- PyMuPDF
- Uvicorn
- Pytest

---

## Project Structure

```
Chatbot/
│
├── main.py
├── .env
├── requirements.txt
│
├── models/
│   └── schemas.py
│
├── routers/
│   ├── ingest.py
│   └── chat.py
│
├── services/
│   ├── embeddings.py
│   ├── chunking.py
│   ├── pdf_reader.py
│   ├── qdrant_service.py
│   ├── groq_service.py
│   ├── history.py
│   └── cache.py
│
├── qdrant_db/
│
└── tests/
    └── test_main.py
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Chatbot
```

Create a virtual environment

```bash
python -m venv ai_venv
```

Activate it

Windows

```bash
ai_venv\Scripts\activate
```

Linux / macOS

```bash
source ai_venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key_here
```

**Do not hardcode the API key.**

---

## Run the Application

```bash
uvicorn main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## POST /ingest

Uploads and indexes a document.

Supports:

- TXT
- PDF

Example:

```
Upload Document.txt
```

Response

```json
{
  "message": "Document ingested successfully."
}
```

---

## POST /chat

Request

```json
{
  "session_id": "user1",
  "query": "What is Artificial Intelligence?"
}
```

Response

```json
{
  "answer": "...",
  "sources": [
    {
      "filename": "Document.txt",
      "chunk_index": 0
    }
  ]
}
```

---

## POST /chat/stream

Returns the answer as a streaming response.

---

# Conversation History

Conversation history is stored using the provided `session_id`.

The chatbot includes the previous **6 conversation turns** in every prompt sent to Groq.

---

# Query Cache

Repeated queries within the same session are returned from an in-memory cache, avoiding unnecessary Groq API calls.

Cache key:

```
session_id + query hash
```

---

# Grounding

The chatbot only answers using retrieved document context.

If the answer cannot be found in the retrieved chunks, it responds:

```
I don't know.
```

---

# Running Tests

Run all tests

```bash
pytest
```

or

```bash
pytest -v
```

Tests include:

- Document ingestion
- Known question
- Unknown question
- Source verification
- Cache verification

---

# Acceptance Criteria

- Upload TXT/PDF documents
- Store embeddings in Qdrant
- Retrieve Top-3 relevant chunks
- Generate grounded answers using Groq
- Return document sources
- Multi-turn conversations
- Query caching
- Streaming responses
- Pytest test suite
- Environment variables loaded from `.env`

