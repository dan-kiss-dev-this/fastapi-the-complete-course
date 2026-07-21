from typing import Annotated

from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

# root folder for fastapi
from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from starlette import status

from models import Users
from database import SessionLocal

from routers.auth import get_current_user, authenticate_user

from .auth import bcrypt_context

# from routers import auth

router = APIRouter(
    prefix='/users',
    tags=['users']
)

class UpdateUser(BaseModel):
    current_password: str
    new_password: str

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

@router.post('/password', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, update_user: UpdateUser):
    # check if password is good
    # if user does not exist raise error
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()


    if not bcrypt_context.verify(update_user.current_password, user_model.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user_model.hashed_password = bcrypt_context.hash(update_user.new_password)
    db.add(user_model)
    db.commit()



