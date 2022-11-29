from fastapi import FastAPI

from app.routers import router

app = FastAPI()

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Welcome to Number Formatter!"}
