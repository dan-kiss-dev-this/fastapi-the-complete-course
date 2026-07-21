from typing import Annotated

from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

# root folder for fastapi
from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from starlette import status

from models import Todos
from database import engine, SessionLocal

from routers.auth import get_current_user

# from routers import auth

router = APIRouter(
    prefix='/admin',
    tags=['admin']
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

# note this path will be /admin/todo based on prefix above
@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    # check if user is admin
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return db.query(Todos).all()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    # check if user is admin
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    deleted_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if deleted_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
    # db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).delete()