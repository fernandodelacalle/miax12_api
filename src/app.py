from fastapi import FastAPI
import typing

app = FastAPI()


@app.post("/insert_name")
def insert_name(name: str):
    pass


@app.get("/names")
def names() -> typing.List[str]:
    return ["pepe", "maria"]
