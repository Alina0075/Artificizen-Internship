import requests

API_URL = "http://localhost:8000"


def auth_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }


def register(email, username, password):
    return requests.post(
        f"{API_URL}/auth/register",
        json={
            "email": email,
            "username": username,
            "password": password
        }
    )


def login(email, password):
    return requests.post(
        f"{API_URL}/auth/login",
        data={
            "username": email,
            "password": password
        }
    )


def get_rooms(token):
    return requests.get(
        f"{API_URL}/rooms",
        headers=auth_headers(token)
    )


def create_room(token, name):
    return requests.post(
        f"{API_URL}/rooms",
        headers=auth_headers(token),
        json={"name": name}
    )


def get_history(token, room_id):
    return requests.get(
        f"{API_URL}/chat/{room_id}/history",
        headers=auth_headers(token)
    )


def delete_history(token, room_id):
    return requests.delete(
        f"{API_URL}/chat/{room_id}/history",
        headers=auth_headers(token)
    )


def get_files(token, room_id):
    return requests.get(
        f"{API_URL}/upload/{room_id}/files",
        headers=auth_headers(token)
    )


def upload_file(token, room_id, uploaded_file):
    return requests.post(
        f"{API_URL}/upload/{room_id}",
        headers=auth_headers(token),
        files={
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }
    )


def send_chat(token, room_id, message):
    return requests.post(
        f"{API_URL}/chat/{room_id}",
        headers=auth_headers(token),
        json={
            "query": message
        }
    )