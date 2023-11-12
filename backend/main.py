from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

# app object
app = FastAPI()

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    change_todo,
    remove_todo,
)

origins = [
    'https://localhost:5173',
    'http://localhost:5173',
    'https://localhost:3000',

    ]

# obligatory CORS handling
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# test
@app.get("/")
async def read_root():
    return {"ping": "pong"}

# get list of todos
@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

# get a single todo by title
@app.get("/api/todo/{title}", response_model=Todo)
async def get_one(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"there is no todo item with the title {title}")

# create a todo
@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Request could not be completed")

# update a single todo
@app.put("/api/todo/{title}", response_model=Todo)
async def update_todo(title:str, desc:str):
    response = await change_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f'there is no todo with the title {title}')

# delete a todo
@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return 'deletion was successful'
    raise HTTPException(404, f'there is no todo with the title {title}')
