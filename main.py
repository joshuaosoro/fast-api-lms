from typing import Union, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API",
    description="Fast API hacking class",
    version="0.0.1",
    contact={
        "name":"joshua",
        "email": "joshuaosoro@gmail.com"
    },
    license_info={
        "name": "MIT",

    }
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Union[str, None] = None

@app.get("/users", response_model=List[User])
async def get_users():
    return users 

@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="ID of user to retrieve"),
    q: str = None
    ):
    if q:
        {"user": users[id], "query": q}
    return {"user": users[id]}

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success"

