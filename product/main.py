from fastapi import FastAPI
prefix ="/product"

app = FastAPI(title="Product API", description="Product API", version="0.1", openapi_url=f"{prefix}/openapi.json", docs_url=f"{prefix}/docs")

@app.get("/product/")
async def root():
    return {'message': 'Hello World From product'}
