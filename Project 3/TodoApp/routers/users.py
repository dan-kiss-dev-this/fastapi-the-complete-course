from typing import Annotated

from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

# root folder for fastapi
from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from starlette import status

from models import Users
from database import engine, SessionLocal

from routers.auth import get_current_user

# from routers import auth

router = APIRouter(
    prefix='/users',
    tags=['users']
)

def get_db():
    # so connect to db and close db connection after response delivered, open db connection only when using database and close after
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get('/')
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")

    return db.query(Users).filter(Users.id == user.get('id')).first()

