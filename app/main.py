from fastapi import FastAPI
from pydantic import BaseModel


class Number(BaseModel):
    input: int | float


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to number formatter. Please visit /docs"}


@app.post("/numbers/")
async def format_number(number: Number):
    return {"formatted": str(number.input)}
