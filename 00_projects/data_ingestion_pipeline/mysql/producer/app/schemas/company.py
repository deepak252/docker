from pydantic import BaseModel
from typing import Optional

class Company(BaseModel):
    name: str
    industry: Optional[str] = None
    country_id: Optional[int] = None


