from datetime import datetime
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, EmailStr


__all__ = ("UserModel",)


class UserModel(BaseModel):
    uuid: str
    username: str
    email: EmailStr
    created_at: datetime
    is_active: bool
    is_superuser: bool


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None