from pydantic import BaseModel
from typing import Literal

class ProductMedia(BaseModel):
    product_id: int
    media_type: Literal["IMAGE", "VIDEO", "PDF"]
    media_url: str
