from fastapi import FastAPI
from .api import router

app = FastAPI(title="Calculator API")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Calculator!"}

#hello