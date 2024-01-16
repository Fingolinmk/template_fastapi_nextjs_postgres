
from fastapi import Depends, APIRouter
from backend.models.user import User
from sqlmodel import Session
from backend.database.database import engine

user_route = APIRouter()

@user_route.post("/users/")
def create_hero(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user