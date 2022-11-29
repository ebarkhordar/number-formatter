from pydantic import BaseModel


class NumberIn(BaseModel):
    input: float


class NumberOut(BaseModel):
    formatted: str
