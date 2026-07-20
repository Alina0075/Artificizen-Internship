# Day 3: Embeddings & Semantic Search

## Overview

This project demonstrates the fundamentals of **Embeddings**, **Semantic Search**, and **Vector Databases**, which are core building blocks of modern AI applications such as Retrieval-Augmented Generation (RAG), AI Assistants, Chatbots, and Document Search Systems.

The project uses the **Sentence Transformers** library to generate embeddings, **NumPy** for cosine similarity calculations, **ChromaDB** for vector storage, and **Qdrant** for production-style semantic search with metadata filtering.

---

## Learning Objectives

After completing this project, I learned how to:

- Understand what text embeddings are.
- Convert text into dense vector representations.
- Measure semantic similarity using cosine similarity.
- Build a semantic search engine.
- Store embeddings in ChromaDB.
- Store embeddings in Qdrant.
- Filter search results using metadata.
- Build reusable embedding utilities for future RAG pipelines.

---

# Technologies Used

- Python 3.13
- Sentence Transformers
- NumPy
- ChromaDB
- Qdrant
- Hugging Face Models

---

# Installation

Create and activate a virtual environment.

```bash
python -m venv ai_venv
```

Windows

```bash
ai_venv\Scripts\activate
```

Install the required packages.

```bash
pip install sentence-transformers
pip install chromadb
pip install qdrant-client
pip install numpy
```

Or install everything together.

```bash
pip install sentence-transformers chromadb qdrant-client numpy
```

---

# Embedding Model

This project uses the following embedding model:

```
all-MiniLM-L6-v2
```

Features:

- 384-dimensional embeddings
- Lightweight (~80 MB)
- Fast inference
- Free to use
- Runs locally
- No API key required

---

# Project Structure

```
Day 3/
│
├── Task1.py
├── Task2.py
├── Task3.py
├── Task4.py
├── Task5.py
├── Task6.py
└── README.md
```

---

# Tasks

## Task 1
### Pairwise Semantic Similarity

Implemented:

- Generated embeddings for six sentences.
- Computed cosine similarity between every pair.
- Ranked sentence pairs from most similar to least similar.

Concepts Covered:

- Sentence embeddings
- Cosine similarity
- Semantic comparison

---

## Task 2
### Semantic Search

Implemented:

- Embedded a user query.
- Embedded multiple documents.
- Compared query with every document.
- Returned the Top-3 most similar documents.

Concepts Covered:

- Query embeddings
- Document embeddings
- Ranking by similarity
- Semantic retrieval

---

## Task 3
### ChromaDB Vector Database

Implemented:

- Created an in-memory ChromaDB collection.
- Stored document embeddings.
- Queried using natural language.
- Retrieved Top-2 results.

Concepts Covered:

- Vector databases
- Collections
- Embedding storage
- Semantic search

---

## Task 4
### Qdrant with Metadata Filtering

Implemented:

- Created an in-memory Qdrant database.
- Stored vectors as points.
- Added payload metadata.
- Filtered results using the source field.

Concepts Covered:

- Qdrant
- Payloads
- Metadata
- Filtering
- Production vector databases

---

## Task 5
### Semantic Search Verification

Implemented:

- Embedded fifty different sentences.
- Queried using completely different wording.
- Verified semantic search retrieves the correct document.

Example

Stored sentence

```
The child is riding a bicycle.
```

Query

```
A kid is cycling.
```

Despite different wording, semantic search correctly identifies the matching document because embeddings capture meaning instead of exact words.

Concepts Covered:

- Semantic understanding
- Synonyms
- Context-aware search
- Embedding quality

---

## Task 6
### Reusable Embedding Utility

Implemented:

Created a reusable function

```python
embed_and_store(texts, metadata_list, collection)
```

The function:

- Batch generates embeddings.
- Creates Qdrant points.
- Stores metadata.
- Upserts vectors into a collection.

Concepts Covered:

- Batch embedding
- Reusable utilities
- Code abstraction
- Production workflow

---

# Cosine Similarity

Cosine similarity measures how similar two vectors are.

Formula

```
Similarity =
A · B
-------------------
||A|| × ||B||
```

Range

| Value | Meaning |
|--------|----------|
| 1 | Identical |
| 0 | Unrelated |
| -1 | Opposite |

Higher cosine similarity indicates greater semantic similarity.

---

# Why Embeddings?

Traditional search

```
Keyword Matching

↓

Exact words only
```

Semantic Search

```
Sentence

↓

Embedding

↓

Meaning

↓

Most Relevant Results
```

Example

Query

```
How can I change my password?
```

Document

```
Use the account recovery page to update your login credentials.
```

Although the wording differs, embeddings identify the semantic similarity.

---

# ChromaDB vs Qdrant

| ChromaDB | Qdrant |
|-----------|---------|
| Beginner-friendly | Production-ready |
| Lightweight | Highly scalable |
| Great for learning | Enterprise applications |
| Easy API | Advanced filtering |
| Rapid prototyping | Large-scale deployments |

---

# Skills Gained

- Embedding generation
- Sentence Transformers
- Cosine similarity
- Semantic search
- Vector databases
- ChromaDB
- Qdrant
- Metadata filtering
- Batch embedding
- Vector storage
- AI retrieval pipelines

---

# Real-World Applications

These techniques are used in:

- Retrieval-Augmented Generation (RAG)
- AI Chatbots
- Document Search
- Enterprise Knowledge Bases
- Question Answering Systems
- Recommendation Systems
- AI Assistants
- Customer Support Bots
- Semantic Search Engines




# License

This project is created for educational and learning purposes.
