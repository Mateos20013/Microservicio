from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse
from services.user_service import UserService
from database import get_db

user_router = APIRouter()

@user_router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db), user_service: UserService = Depends()):
    return user_service.create_user(user, db)

@user_router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), user_service: UserService = Depends()):
    user = user_service.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
