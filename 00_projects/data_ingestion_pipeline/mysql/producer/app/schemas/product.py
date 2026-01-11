from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

class Product(BaseModel):
    company_id: int
    media_channel_id: int
    country_id: int

    title: str
    description: Optional[str] = None
    category: Optional[str] = None

    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: Optional[Decimal] = None
