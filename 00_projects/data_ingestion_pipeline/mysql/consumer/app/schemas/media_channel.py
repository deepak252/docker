from pydantic import BaseModel
from datetime import datetime

class MediaChannelBase(BaseModel):
    name: str
    type: str

class MediaChannelCreate(MediaChannelBase):
    pass

class MediaChannelResponse(MediaChannelBase):
    id: int
    created_at: datetime

    class Config:
        # Tells Pydantic to read data not just from dicts
        # but also from ORM objects (like SQLAlchemy models)
        from_attributes = True