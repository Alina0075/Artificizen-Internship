import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_ingest_document():

    sample_text = """
Artificial Intelligence is the simulation of human intelligence.

Machine Learning is a subset of AI.

Deep Learning uses neural networks.
"""
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write(sample_text)
    with open("sample.txt", "rb") as file:
        response = client.post(
            "/ingest",
            files={
                "file": (
                    "sample.txt",
                    file,
                    "text/plain"
                )
            }
        )

    os.remove("sample.txt")
    assert response.status_code == 200
    data = response.json()
    assert "messages" in data
    assert data["filename"] == "sample.txt"
    assert data["chunks"] > 0

def test_known_question():
    response = client.post(
        "/chat",
        json={
            "session_id": "pytest",
            "query": "What is AI?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "sources" in data
    
def test_unknown_question():
    response = client.post(
        "/chat",
        json={
            "session_id": "pytest",
            "query": "Who invented Facebook?"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert (
        "don't know" in data["answer"].lower()
        or
        "do not know" in data["answer"].lower()
    )

def test_sources_returned():

    response = client.post(
        "/chat",
        json={
            "session_id": "pytest",
            "query": "What is AI?"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["sources"]) > 0
    
def test_cache_hit():
    payload = {
        "session_id": "cache_test",
        "query": "What is AI?"
    }
    first = client.post(
        "/chat",
        json=payload
    )
    second = client.post(
        "/chat",
        json=payload
    )
    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json()["answer"] == second.json()["answer"]