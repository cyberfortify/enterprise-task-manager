from fastapi import APIRouter, Depends, HTTPException, Header
from jose import jwt
from sqlalchemy.orm import Session
from task_service.schemas import TaskCreate, TaskUpdate
from task_service.database import SessionLocal, engine
from task_service.models import Task, Base

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(auth_header: str):
    try:
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["user_id"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/tasks")
def create_task(task: TaskCreate, authorization: str = Header(...), db: Session = Depends(get_db)):
    user_id = verify_token(authorization)

    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=user_id
    )

    db.add(new_task)
    db.commit()
    return {"message": "Task created"}


@router.get("/tasks")
def get_tasks(authorization: str = Header(...), db: Session = Depends(get_db)):
    user_id = verify_token(authorization)
    return db.query(Task).filter(Task.user_id == user_id).all()