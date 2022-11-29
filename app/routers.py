from fastapi import APIRouter

from app.schemas import Number
from app.services import formatter

router = APIRouter()


@router.post("/numbers/")
async def number_formatter(number: Number):
    formatted = formatter(number.input)
    return {"formatted": formatted}
