from fastapi.testclient import TestClient
from user_service.main import app
import uuid

client = TestClient(app)

def test_signup():
    unique_user = str(uuid.uuid4())

    response = client.post("/signup", json={
        "username": unique_user,
        "password": "1234"
    })

    assert response.status_code == 200

def test_login():
    response = client.post("/login", json={
        "username": "testuser",
        "password": "1234"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()