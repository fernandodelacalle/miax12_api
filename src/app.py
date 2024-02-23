from fastapi import FastAPI
import typing
from pymongo import MongoClient

app = FastAPI()


@app.post("/insert_name")
def insert_name(name: str):
    # conectar al Mongo=mongodb://root:example@mongo:27017
    mongo_dir = 'mongodb://root:example@mongo:27017'
    client = MongoClient(mongo_dir)
    db = client['test_db']
    col = db['test_coll']
    col.insert_one({'name':'test2'})
    pass


@app.get("/names")
def names() -> typing.List[str]:
    return ["pepe", "maria"]
