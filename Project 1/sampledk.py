from fastapi import FastAPI

app = FastAPI()

# GET Route
@app.get("/")
def read_root():
    return{"message": "Hello from FastAPI"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.post("/users")
def create_user(user: dict):
    return {
        "message": "User created",
        "data": user
    }

