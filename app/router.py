from fastapi import APIRouter

from app.schemas import Number

router = APIRouter()


@router.post("/numbers/")
async def format_number(number: Number):
    return {"formatted": str(number.input)}
