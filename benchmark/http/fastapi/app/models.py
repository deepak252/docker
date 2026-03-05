from pydantic import BaseModel
from typing import Dict


class ApiData(BaseModel):
    url: str
    method: str


class WrkResult(BaseModel):
    url: str
    method: str
    connections: int
    time_taken: str
    total_hits: int
    success_hits: int
    failure_hits: int
    success_messages: Dict[int, int]
    failure_messages: Dict[int, int]