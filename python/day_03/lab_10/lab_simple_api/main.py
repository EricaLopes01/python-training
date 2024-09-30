# src/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/custom")
async def custom_message():
    return {"message": "This is a custom message!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/greet/")
async def greet(name: str = "World"):
    return {"message": f"Hello, {name}!"}

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str

@app.post("/items/")
async def create_item(item: Item):
    return item

