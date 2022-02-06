from fastapi import FastAPI
prefix ="/cart"

app = FastAPI(title="Cart API", description="Cart API", version="0.1", openapi_url=f"{prefix}/openapi.json", docs_url=f"{prefix}/docs")

@app.get("/cart/")
async def root():
    return {'message': 'Hello World From cart'}
