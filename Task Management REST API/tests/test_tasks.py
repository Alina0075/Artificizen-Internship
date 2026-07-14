def create_user(client):
    client.post("/auth/register",json={"username":"alina","password":"password123"})

def login(client):
    response=client.post("/auth/login",data={"username":"alina","password":"password123"})
    token=response.json()["access_token"]
    return{"Authorization": f"Bearer {token}"}

def test_create_tast(client):
    create_user(client)
    headers=login(client)
    response=client.post("/tasks/",headers=headers, json={"title":"FastAPI Project",
                        "description": "Complete capston","status":"pending","due_date":"2026-08-01"})
    assert response.status_code==200
    assert response.json()["title"]=="FastAPI Project"
    
def test_get_tasks(client):
    create_user(client)
    headers=login(client)
    client.post("/tasks/",headers=headers,json={"title":"Task One",
                        "description": "Description","status":"pending","due_date":"2026-08-01"})
    response=client.get("/tasks/",headers=headers)
    assert response.status_code==200
    assert len(response.json())==1

def test_filter_tasks(client):
    create_user(client)
    headers=login(client)
    client.post("/tasks/",headers=headers,json={"title":"Task1",
                        "description": "Desc","status":"pending","due_date":"2026-08-01"})
    client.post("/tasks/",headers=headers,json={"title":"Task2",
                        "description": "Desc","status":"done","due_date":"2026-08-01"})
    response=client.get("/tasks/?status=done",headers=headers)
    assert response.status_code==200
    tasks=response.json()
    assert len(tasks)==1
    assert tasks[0]["status"]=="done"

def test_unauthorized_access(client):
    response=client.get("/tasks/")
    assert response.status_code==401
    
def test_delete_task(client):
    create_user(client)
    headers=login(client)
    response=client.post("/tasks/",headers=headers,json={"title":"Delete Me",
                        "description": "Testing delete","status":"pending","due_date":"2026-08-01"})
    task_id=response.json()["id"]
    response=client.delete(f"/tasks/{task_id}",headers=headers)
    assert response.status_code==200
    assert response.json()["message"]=="Task deleted successfully"
    
    