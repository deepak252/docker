from pydantic import BaseModel
from datetime import datetime

class CountryBase(BaseModel):
    name: str
    iso_code: str

class CountryCreate(CountryBase):
    pass

class CountryResponse(CountryBase):
    id: int
    created_at: datetime

    class Config:
        # Tells Pydantic to read data not just from dicts
        # but also from ORM objects (like SQLAlchemy models)
        from_attributes = True