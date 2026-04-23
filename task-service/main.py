from fastapi import FastAPI
from routes import router

app = FastAPI(title="Task Service")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Task Service Running"}