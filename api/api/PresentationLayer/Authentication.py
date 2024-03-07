from fastapi import APIRouter, Depends, Request
from .dependencies import get_authenticator

router = APIRouter()


@router.get("/login")
async def default(request: Request, authenticator=Depends(get_authenticator)):
    """_summary_

    Returns:
        _type_: _description_
    """

    return [{"default": "success"}]
