from pydantic import BaseModel
from typing import Any, Optional

class ApiResponse(BaseModel):
    message: str = "success"
    data: Optional[Any] = None
