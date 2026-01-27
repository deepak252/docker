from pydantic import BaseModel
from datetime import date


class Product(BaseModel):
    product_id: int
    name: str
    category: str
    price: float
    in_stock: bool
    created_at: date
