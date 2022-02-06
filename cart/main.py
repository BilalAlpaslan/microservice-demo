from fastapi import FastAPI

app = FastAPI(title="Cart API", description="Cart API", version="0.1", root_path="/cart")


@app.get("/")
async def root():
    return {'message': 'Hello World From cart'}
