from typing import Union, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api import users, sections, courses

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

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)

