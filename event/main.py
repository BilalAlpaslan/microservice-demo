from fastapi import FastAPI

app = FastAPI(title="Event API", description="Event API", version="0.1", root_path="/event")


@app.get("/")
async def root():
    return {'message': 'Hello World From event'}
