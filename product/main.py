from fastapi import FastAPI

app = FastAPI(title="Product API", description="Product API", version="0.1", root_path="/product")


@app.get("/")
async def root():
    return {'message': 'Hello World From product'}
