from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String
from sqlmodel import Field, SQLModel

__all__ = ("User",)


class User(SQLModel, table=True):
    uuid: str = Field(default=str(uuid4()),primary_key=True,index=True,nullable=False)
    username: str = Field(sa_column=Column(String,unique=True,nullable=False))
    email: str = Field(sa_column=Column(String,unique=True,nullable=False))
    password_hash: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    is_active: bool = Field(default=True,nullable=False)
    is_superuser: bool = Field(default=False,nullable=False)
