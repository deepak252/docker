from fastapi import APIRouter, Depends
from app.schemas.media_channel import MediaChannel
from app.core.response import ApiResponse
from app.core.dependencies import  get_media_channel_service
from app.services.media_channel_service import MediaChannelService

router = APIRouter(prefix="/mchannels", tags=["Media Channel"])

@router.post("/", response_model=ApiResponse)
def create_media_channel(payload: MediaChannel, service: MediaChannelService = Depends(get_media_channel_service)):
    service.publish_media_channel(payload)
    return ApiResponse(message="Media channel published", data=payload)

@router.post("/produce", response_model=ApiResponse)
def produce_media_channels(service: MediaChannelService = Depends(get_media_channel_service)):
    cnt = service.produce_media_channels()
    return ApiResponse(message="Media channels published", data={
        "count": cnt
    })