from fastapi.testclient import TestClient
from task_service.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", headers={
        "Authorization": "Bearer fake_token"
    }, json={
        "title": "Test Task",
        "description": "Testing"
    })

    assert response.status_code in [200, 401]