from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse
from models import User
from abc import ABC, abstractmethod

class IUserService(ABC):
    @abstractmethod
    def create_user(self, user: UserCreate, db: Session):
        pass

    @abstractmethod
    def get_user(self, user_id: int, db: Session):
        pass

class UserService(IUserService):
    def create_user(self, user: UserCreate, db: Session):
        new_user = User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_user(self, user_id: int, db: Session):
        return db.query(User).filter(User.id == user_id).first()
