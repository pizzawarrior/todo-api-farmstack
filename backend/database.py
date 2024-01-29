from model import Todo
from dotenv import load_dotenv
import os

# MongoDB driver:
import motor.motor_asyncio


load_dotenv()

my_id = os.getenv("CONNECTION_STRING")

client = motor.motor_asyncio.AsyncIOMotorClient({my_id})
database = client.get_database("TodoList")
collection = database.get_collection("todo")


# Get one todo:
async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document


# Get list of todos:
async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def change_todo(title, desc):
    # find the todo by title, and we will update the description using $set
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document


async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True
