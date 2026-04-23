from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from user_service.schemas import UserCreate
from jose import jwt
from datetime import datetime, timedelta, timezone
from user_service.database import SessionLocal, engine
from user_service.models import User, Base

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

def create_token(data: dict):
    to_encode = data.copy()
    from datetime import datetime, timezone
    expire = datetime.now(timezone.utc) + timedelta(hours=2)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()

    return {"message": "User created"}

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user_id": db_user.id})
    
    return {"access_token": token}