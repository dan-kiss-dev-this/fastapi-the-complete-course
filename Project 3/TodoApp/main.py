from typing import Annotated
from sqlalchemy.orm import Session

# root folder for fastapi
from fastapi import FastAPI, Depends
import models
from models import Todos
from database import engine, SessionLocal



app = FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    # so connect to db and close db connection after response delivered, open db connection only when using database and close after
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# note Depends below is dependency injection
@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()


# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



# from fastapi import FastAPI
# import models
# from database import engine
# from routers import auth, todos, admin, users
#
# app = FastAPI()
#
# models.Base.metadata.create_all(bind=engine)
#
# app.include_router(auth.router)
# app.include_router(todos.router)
# app.include_router(admin.router)
# app.include_router(users.router)