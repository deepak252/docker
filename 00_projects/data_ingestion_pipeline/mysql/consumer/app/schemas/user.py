from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        # Tells Pydantic to read data not just from dicts
        # but also from ORM objects (like SQLAlchemy models)
        from_attributes = True