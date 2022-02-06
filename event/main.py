from fastapi import FastAPI
app = FastAPI()


@app.get('/event/')
async def root():
    return {'message': 'Hello World From event app'}
