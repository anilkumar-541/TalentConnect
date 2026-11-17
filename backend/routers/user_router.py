from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from database import get_db
from schemas.user_schema import UserCreate,UserResponse
from services.user_service import register_user

router = APIRouter(
    prefix= "/Users",
    tags =["Users"]
)

@router.post(
    "/register",
    response_model = UserResponse,
    status_code=status.HTTP_201_CREATED
)

def create_user(
    user_data: UserCreate,
    db:Session= Depends(get_db)
):
    new_user = register_user(db,user_data)

    if new_user is None:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email already registered"
        )
    return new_user