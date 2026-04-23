from fastapi import FastAPI
from user_service.auth import router as auth_router

app = FastAPI(title="User Service")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "User Service Running"}