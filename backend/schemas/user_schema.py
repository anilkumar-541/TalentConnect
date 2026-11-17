from pydantic import BaseModel,Field
from typing import Literal

class UserCreate(BaseModel):
    full_name: str = Field(min_length=2,max_length=100)
    email : str = Field(max_length=150)
    password: str = Field(min_length=8)
    phone_number:str | None = None
    role: Literal["customer","provider"] = "customer"

class UserResponse(BaseModel):
    id: int
    full_name: str
    email :str
    phone_number:str | None
    role: str
    is_active: bool

    model_config = {"from_attributes":True}