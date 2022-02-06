from fastapi import FastAPI
prefix ="/event"
app = FastAPI(title="Event API", description="Event API", version="0.1", openapi_url=f"{prefix}/openapi.json", docs_url=f"{prefix}/docs")

@app.get('/event/')
async def root():
    return {'message': 'Hello World From event app'}
