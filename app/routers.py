from fastapi import APIRouter

from app.schemas import NumberIn, NumberOut
from app.services import formatter

router = APIRouter()


@router.post(
    "/numbers/",
    response_model=NumberOut,
    summary="Prettify a number",
)
async def number_formatter(number: NumberIn):
    """
    Prettify a number:

    - **formatted**: truncated and prettified string version of input number
    """
    formatted = formatter(number.input)
    return NumberOut(formatted=formatted)
