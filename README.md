# 🛡️ CyberRAG — Multimodal Cybersecurity Intelligence Platform

## Capstone Project - Multimodal RAG

CyberRAG is a **multimodal Retrieval-Augmented Generation (RAG) platform** designed for cybersecurity intelligence and evidence analysis.

Users can create investigation workspaces, upload cybersecurity-related documents and media, and ask natural-language questions about the uploaded evidence.

### Core Technologies

* **FastAPI** — Backend REST API
* **Streamlit** — Frontend
* **Sentence Transformers** — Semantic embeddings
* **Qdrant** — Vector storage and similarity search
* **Groq** — LLM inference
* **PostgreSQL** — Application data and chat history
* **Alembic** — Database migrations

CyberRAG follows a grounded RAG workflow. Answers are generated only from retrieved evidence. If the evidence does not contain the answer, the system returns:

```text
I don't know.
```

with an empty source list.

---

# 🚀 How to Run

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd CyberRag
```

## 2. Create and Activate Virtual Environment

Windows:

```powershell
python -m venv ai_venv
.\ai_venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your_secret_key
DATABASE_URL=your_postgresql_database_url
```

**Never commit `.env` to GitHub.**

The `.gitignore` excludes secrets, virtual environments, uploads, Qdrant storage, databases, and cache files.

## 5. Database Setup

Make sure PostgreSQL is running and the configured database exists.

Run migrations:

```bash
alembic upgrade head
```

Check the current migration:

```bash
alembic current
```

## 6. Start Backend

```bash
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 7. Start Streamlit

```bash
streamlit run streamlit/streamlit.py
```

### Quick Start

```powershell
.\ai_venv\Scripts\Activate.ps1
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
streamlit run streamlit/streamlit.py
```

---

# 🎯 Industry Use Case

CyberRAG is designed as a **Cybersecurity Evidence and Intelligence Workspace**.

### Target Users

* Cybersecurity analysts
* SOC analysts
* Security researchers
* Incident response teams
* Cybersecurity students
* IT security teams

### Example Evidence

Users can upload:

* Security reports
* Threat intelligence documents
* Incident documentation
* Presentations
* CSV datasets
* Screenshots
* Audio/video evidence
* Investigation notes

Each investigation is isolated within its own workspace.

---

# ✨ Key Features

## 🔐 Authentication

* User registration and login
* Password hashing
* JWT authentication
* Protected API endpoints
* Owner-scoped workspaces

## 🏠 Investigation Workspaces

Users can:

* Create workspaces
* Upload evidence
* Ask questions
* View chat history
* Delete conversations
* Delete workspaces

## 📁 Multimodal File Support

| Format     | Extensions                       |
| ---------- | -------------------------------- |
| PDF        | `.pdf`                           |
| Word       | `.docx`                          |
| Images     | `.png`, `.jpg`, `.jpeg`          |
| Audio      | `.mp3`, `.wav`, `.flac`          |
| Video      | `.mp4`, `.avi`, `.mov` |
| PowerPoint | `.pptx`                          |
| CSV        | `.csv`                           |
| Markdown   | `.md`                            |
| Text       | `.txt`                           |

---

# 🔄 Multimodal Ingestion Pipeline

```text
User Upload
     │
     ▼
FastAPI Upload Endpoint
     │
     ▼
File Type Detection
     │
     ▼
Content Extraction
     │
     ▼
Chunking
     │
     ▼
Sentence Transformer
     │
     ▼
Qdrant Vector Store
```

Each chunk contains metadata such as workspace, file, and chunk information for traceable retrieval.

---

# 🧠 RAG Pipeline

```text
User Question
      │
      ▼
Query Embedding
      │
      ▼
Qdrant Similarity Search
      │
      ▼
Top 5 Relevant Chunks
      │
      ▼
Workspace Filtering
      │
      ▼
Conversation History
      │
      ▼
Groq LLM
      │
      ▼
Answer + Sources
      │
      ▼
PostgreSQL Chat History
```

Retrieval is filtered using `room_id` so evidence from another workspace cannot be included.

---

# 🤖 Grounded Generation

The assistant is instructed to answer only from retrieved evidence:

```text
You are a cybersecurity intelligence assistant.
Answer ONLY using the provided context.
If the answer is not in the context, reply exactly:
I don't know.
Do not use outside knowledge.
Do not make up information.
```

If no relevant evidence is found:

```json
{
    "answer": "I don't know.",
    "sources": []
}
```

---

# 📚 Source Tracking

Every grounded response includes source information:

```json
{
    "filename": "security_report.pdf",
    "file_type": "pdf",
    "chunk_index": 4,
    "excerpt": "Relevant extracted text..."
}
```

The Streamlit interface displays the sources below the assistant's response.

---

# 💬 Chat History

Conversations are stored in PostgreSQL.

Each message contains:

* Message ID
* Workspace ID
* User ID
* Role
* Content
* Sources
* Timestamp

The latest conversation messages are included as context for subsequent questions.

---

# 🔎 Retrieval System

CyberRAG uses:

```text
Embedding Model: all-MiniLM-L6-v2
Vector Database: Qdrant
Top K Retrieval: 5
```

Semantic embeddings allow the system to retrieve relevant information even when the user's wording differs from the original document.

---

# 🖼️ Multimodal Processing

Different file types are processed through dedicated extractors:

* **PDF** — Text extraction
* **DOCX** — Paragraph and table extraction
* **Images** — Vision/multimodal processing
* **Audio** — Transcription
* **Video** — Audio extraction and transcription
* **PPTX** — Slide text extraction
* **CSV** — Structured data processing
* **Markdown/TXT** — Direct text processing

Extracted content is converted into searchable chunks and stored in Qdrant.

---

# 🌐 API

The FastAPI backend provides the following main endpoint groups:

```text
/auth
/rooms
/upload
/chat
```

### Authentication

```http
POST /auth/register
POST /auth/login
```

### Workspaces

```http
GET /rooms
POST /rooms
DELETE /rooms/{room_id}
```

### Upload

```http
POST /upload/{room_id}
```

### Chat

```http
POST /chat/{room_id}
GET /chat/{room_id}/history
DELETE /chat/{room_id}/history
```

Swagger documentation is available at:

```text
/docs
```

---

# 🗄️ Database Architecture

CyberRAG uses PostgreSQL with SQLAlchemy.

### Main Models

```text
User
 ├── ChatRoom
 │     ├── ChatMessage
 │     └── UploadedFile
 └── ChatMessage
```

### User

```text
id
username
email
hashed_password
created_at
```

### ChatRoom

```text
id
name
description
owner_id
created_at
```

### ChatMessage

```text
id
room_id
user_id
role
content
sources
created_at
```

### UploadedFile

```text
id
room_id
filename
file_type
file_path
status
error_message
uploaded_at
```

---

# 🖥️ Project Structure

```text
CyberRag/
│
├── alembic/
│   └── versions/
│
├── app/
│   ├── database/
│   ├── routers/
│   ├── schemas/
│   └── services/
│       └── ingestion/
│
├── streamlit/
│   ├── api.py
│   ├── streamlit.py
│   └── styles.py
│
├── demo files/
│
├── docs/
│   └── CyberRAG_Architecture_v2.drawio (1).png
│
├── requirements.txt
├── alembic.ini
├── .gitignore
└── README.md
```

---

# 🛠️ Technology Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Frontend        | Streamlit             |
| Backend         | FastAPI               |
| API Server      | Uvicorn               |
| Database        | PostgreSQL            |
| ORM             | SQLAlchemy            |
| Migrations      | Alembic               |
| Vector Database | Qdrant                |
| Embeddings      | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2      |
| LLM             | Groq                  |
| LLM Model       | Llama 3.3 70B         |
| Authentication  | JWT                   |
| PDF             | PyMuPDF               |
| DOCX            | python-docx           |
| PPTX            | python-pptx           |
| CSV             | pandas                |
| Language        | Python                |

---

# 🏗️ Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 │ REST API + JWT
 ▼
FastAPI Backend
 │
 ├── Authentication
 ├── Workspaces
 ├── Upload
 └── Chat
       │
       ├──────────────► PostgreSQL
       │
       ▼
 Multimodal Ingestion
       │
       ▼
 Text Extraction
       │
       ▼
 Chunking
       │
       ▼
 Sentence Transformers
       │
       ▼
 Qdrant
       │
       ▼
 RAG Prompt + History
       │
       ▼
 Groq LLM
       │
       ▼
 Answer + Sources
```

Architecture documentation is available under:

```text
docs/
```

---

# 🔒 Security

CyberRAG implements several security practices:

* Password hashing
* JWT authentication
* Protected API endpoints
* Workspace ownership checks
* Workspace-filtered vector retrieval
* Environment-based secrets
* Grounded LLM responses

Sensitive files and generated data are excluded using `.gitignore`.

Never commit:

```text
.env
GROQ_API_KEY
DATABASE_PASSWORD
SECRET_KEY
```

---

# 🧪 Example Questions

Users can ask questions such as:

```text
What cybersecurity practices are recommended?
```

```text
What threats are mentioned in the uploaded report?
```

```text
Summarize the cybersecurity recommendations.
```

```text
What information is contained in the uploaded table?
```

```text
What does the presentation say about password security?
```

For questions not supported by the uploaded evidence:

```text
I don't know.
```

---

# 📊 Demo Evidence

Demo files are available under:

```text
demo files/
```

The collection includes cybersecurity awareness material and multiple supported formats, including documents, images, audio, video, Markdown, and structured data.

---

# 🧪 Testing Checklist

Before demonstration, verify:

* [ ] Registration and login
* [ ] JWT authentication
* [ ] Workspace creation/deletion
* [ ] File upload and processing
* [ ] Multimodal extraction
* [ ] Qdrant retrieval
* [ ] Workspace filtering
* [ ] Groq generation
* [ ] Grounded responses
* [ ] Source display
* [ ] Chat history
* [ ] Swagger API documentation

---

# 📋 Week 4 Capstone Requirements

### Day 1 — Architecture

* Cybersecurity industry positioning
* System architecture
* Streamlit + FastAPI architecture
* PostgreSQL and Qdrant integration

### Day 2 — Backend

* FastAPI backend
* Authentication
* PostgreSQL
* SQLAlchemy
* Alembic
* Workspace and chat APIs

### Day 3 — Multimodal Ingestion

Support for:

```text
PDF | DOCX | Image | Audio | Video | PPTX | CSV | MD | TXT
```

### Day 4 — RAG + Frontend

* Qdrant retrieval
* Sentence Transformers
* Groq LLM
* Grounded generation
* Sources
* Chat persistence
* Streamlit interface

### Day 5 — Finalization

* Frontend improvements
* Documentation
* Architecture diagram
* Demo evidence
* Repository organization

---

# 🚧 Limitations

Current limitations may include:

* OCR/vision quality for complex images
* Transcription accuracy for noisy audio/video
* Complex document layouts
* Highly structured spreadsheets
* Very large files
* External API availability

---

# 🔮 Future Improvements

Potential improvements include:

* Role-based access control
* Multi-user workspaces
* S3-compatible storage
* Advanced OCR
* Improved table extraction
* Streaming LLM responses
* Threat intelligence integrations
* SOC platform integration
* Advanced audit logging
* Docker deployment
* CI/CD pipeline
* Rate limiting

---

# 📦 Dependencies

Main dependencies include:

```text
fastapi
uvicorn
streamlit
sqlalchemy
alembic
python-dotenv
python-jose
passlib
bcrypt
groq
sentence-transformers
qdrant-client
python-docx
python-pptx
pandas
PyMuPDF
moviepy
```

The complete dependency list is available in:

```text
requirements.txt
```

Install with:

```bash
pip install -r requirements.txt
```

---

# 👩‍💻 Project Information

|                    |                         |
| ------------------ | ----------------------- |
| **Project**        | CyberRAG                |
| **Capstone**       | Week 4 — Multimodal RAG |
| **Industry**       | Cybersecurity           |
| **Backend**        | FastAPI                 |
| **Frontend**       | Streamlit               |
| **Database**       | PostgreSQL              |
| **Vector Store**   | Qdrant                  |
| **Embeddings**     | Sentence Transformers   |
| **LLM**            | Groq — Llama 3.3 70B    |
| **Authentication** | JWT                     |
| **Migrations**     | Alembic                 |

---

# 🏁 Conclusion

CyberRAG demonstrates a practical **multimodal RAG system for cybersecurity intelligence and evidence analysis**.

It combines authentication, investigation workspaces, multimodal ingestion, semantic search, vector retrieval, conversation history, grounded LLM generation, and source attribution into a single platform.

The system enables users to upload diverse cybersecurity evidence, ask natural-language questions, and receive evidence-based answers with traceable sources.
