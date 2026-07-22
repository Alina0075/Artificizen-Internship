# RAG with FastAPI

A Retrieval-Augmented Generation (RAG) application built using FastAPI, Groq LLM, Sentence Transformers, and Qdrant Vector Database.

## Overview

This project implements a complete RAG pipeline where user queries are enhanced with external knowledge before being sent to an LLM for generating accurate and context-aware responses.

The workflow:

1. User provides a query.
2. Query is converted into an embedding.
3. Similar information is retrieved from Qdrant Vector Database.
4. Retrieved context is added to the prompt.
5. Groq LLM generates the final response.

## Tech Stack

- Python
- FastAPI
- Groq API
- Sentence Transformers
- Qdrant Vector Database
- Uvicorn
- Python-dotenv

## Project Structure

```
RAG-FastAPI/
│
├── main.py
├── rag.py
├── embeddings.py
├── vector_db.py
│
├── documents/
│   └── knowledge.txt
│
├── .env
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd RAG-FastAPI
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

## RAG Pipeline

### 1. Document Processing

Documents are loaded from the knowledge base and converted into embeddings using a Sentence Transformer model.

### 2. Embedding Generation

Text is converted into numerical vectors that represent semantic meaning.

Example:

```
Text
 |
 v
Embedding Vector
```

### 3. Vector Storage

Generated embeddings are stored in Qdrant Vector Database.

Qdrant enables fast similarity search between vectors.

### 4. Retrieval

When a user asks a question, the query is converted into an embedding and compared with stored document embeddings.

The most relevant documents are retrieved.

### 5. Generation

The retrieved information is added to the prompt and passed to the Groq LLM.

The LLM generates the final answer based on the provided context.

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides automatic Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoint

### Ask Question

POST:

```
/ask
```

Request:

```json
{
    "question": "What is Artificial Intelligence?"
}
```

Response:

```json
{
    "answer": "Artificial Intelligence is..."
}
```

## Key Concepts

### Embeddings

Embeddings convert text into numerical representations that capture meaning and relationships between words and sentences.

### Vector Database

A database optimized for storing and searching embeddings using similarity calculations.

### Semantic Search

Semantic search retrieves information based on meaning rather than exact keyword matching.

### Retrieval-Augmented Generation

RAG improves LLM responses by providing additional external knowledge.

Benefits:

- Reduces hallucinations
- Uses custom data
- Improves accuracy
- Enables domain-specific AI applications

## Future Improvements

- Add PDF document support
- Add document chunking strategies
- Add conversation memory
- Add authentication
- Add Docker deployment
- Deploy on cloud infrastructure
- Add streaming responses

## Learning Outcomes

After completing this project:

- Understand RAG architecture
- Build AI APIs using FastAPI
- Generate and use embeddings
- Work with vector databases
- Perform semantic search
- Integrate LLMs with external knowledge


AI Engineer Intern 
