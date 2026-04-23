from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="API Gateway")

USER_SERVICE = "http://127.0.0.1:8001"
TASK_SERVICE = "http://127.0.0.1:8002"

# Forward request function
async def forward_request(method, url, headers=None, json=None):
    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, headers=headers, json=json)
        return response.json()

# ---------------- USER ROUTES ---------------- #

@app.post("/signup")
async def signup(request: Request):
    body = await request.json()
    return await forward_request("POST", f"{USER_SERVICE}/signup", json=body)

@app.post("/login")
async def login(request: Request):
    body = await request.json()
    return await forward_request("POST", f"{USER_SERVICE}/login", json=body)

# ---------------- TASK ROUTES ---------------- #

@app.post("/tasks")
async def create_task(request: Request):
    body = await request.json()
    token = request.headers.get("Authorization")

    headers = {"Authorization": token} if token else {}

    return await forward_request("POST", f"{TASK_SERVICE}/tasks", headers=headers, json=body)

@app.get("/tasks")
async def get_tasks(request: Request):
    token = request.headers.get("Authorization")

    headers = {"Authorization": token} if token else {}

    return await forward_request("GET", f"{TASK_SERVICE}/tasks", headers=headers)