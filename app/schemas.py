from pydantic import BaseModel


class Number(BaseModel):
    input: float
