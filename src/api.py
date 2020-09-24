from src import app


@app.get("/")
async def hello_world():
    return {"OK": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}