def test_register(client):
    response=client.post("/auth/register",json={"username":"alina","password":"password123"})
    assert response.status_code==200
    data=response.json()
    assert data["username"]=="alina"
    assert "id" in data

def test_register_duplicate_username(client):
    client.post("/auth/register",json={"username":"alina","password":"password123"})
    response=client.post("/auth/register",json={"username":"alina","password":"password123"})
    assert response.status_code==400
    assert response.json()["detail"]=="Username already exists"
    
def test_login(client):
    client.post("/auth/register",json={"username":"alina","password":"password123"})
    response=client.post("/auth/login",data={"username":"alina","password":"password123"})
    assert response.status_code==200
    token = response.json()
    assert token["token_type"]=="bearer"
    assert "access_token" in token

def test_login_wrong_password(client):
    client.post("/auth/register",json={"username":"alina","password":"password123"})
    response=client.post("/auth/login",data={"username":"alina", "password":"wrongpassword"})
    assert response.status_code==401
    