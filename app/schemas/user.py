from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(..., example="johndoe")
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., example="strongpassword123")


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4


class UserInDb(User):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
