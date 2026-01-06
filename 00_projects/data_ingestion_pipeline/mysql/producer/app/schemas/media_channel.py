from pydantic import BaseModel, Field
from typing import List

class MediaChannel(BaseModel):
    name: str
    type: str

class MediaChannelListPayload(BaseModel):
    media_channels: List[MediaChannel]