from fastapi import FastAPI
import typing
from pymongo import MongoClient
import os

app = FastAPI()


@app.post("/insert_name")
def insert_name(name: str):
    client = MongoClient(os.getenv("MONGO_ADDR"))
    db = client['DB_API']
    col = db['nombres']

    # Check if name already exists in the collection
    existing_entry = col.find_one({'name': name})
    if existing_entry:
        print(f"The name '{name}' already exists in the collection.")
    else:
        col.insert_one({'name': name})
        print(f"The name '{name}' has been inserted into the collection.")


@app.get("/names")
def names() -> typing.List[str]:
    client = MongoClient(os.getenv("MONGO_ADDR"))
    db = client['DB_API']
    col = db['nombres']

    documents = col.find({"name": {"$exists": True}})
    return [doc['name'] for doc in documents]
