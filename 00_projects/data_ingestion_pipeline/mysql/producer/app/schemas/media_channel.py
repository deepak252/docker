from pydantic import BaseModel

class MediaChannel(BaseModel):
    name: str
    type: str
