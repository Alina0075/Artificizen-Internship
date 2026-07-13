from fastapi.testclient import TestClient
from main import app
from routers.users import fake_db

client = TestClient(app)

def setup_function():
    fake_db.clear()

def test_create_user():

    response = client.post(
        "/users/",
        json={
            "name": "Alina",
            "email": "alina@gmail.com"
        }
    )

    assert response.status_code == 201
    assert response.json()["email"] == "alina@gmail.com"

def test_duplicate_email():

    user = {
        "name": "Alina",
        "email": "alina@gmail.com"
    }

    client.post("/users/", json=user)

    response = client.post("/users/", json=user)

    assert response.status_code == 409
    assert response.json()["detail"] == "Email already exists"
def test_protected_route():

    response = client.get("/users/me")

    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"