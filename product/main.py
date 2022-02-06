from fastapi import APIRouter, FastAPI
prefix ="/product/api"

app = FastAPI(title="Product API", description="Product API", version="0.1", openapi_url=f"{prefix}/openapi.json", docs_url=f"{prefix}/docs")

router = APIRouter()
app.include_router(router, prefix=prefix)

@router.get("/")
async def root():
    return {'message': 'Hello World From product'}
