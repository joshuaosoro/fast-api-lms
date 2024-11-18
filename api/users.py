from typing import List, Union
from pydantic import BaseModel
import fastapi

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Union[str, None] = None

@router.get("/users", response_model=List[User])
async def get_users():
    return users 

@router.get("/users/{id}")
async def get_user():    
    return {"user": users[id]}

@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success"

