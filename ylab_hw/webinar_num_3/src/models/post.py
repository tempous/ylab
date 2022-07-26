from datetime import datetime
from typing import Optional
from uuid import UUID
from sqlmodel import Field, SQLModel

__all__ = ("Post",)


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    views: int = Field(default=0)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    user_id: str = Field(nullable=False, foreign_key='user.uuid')
