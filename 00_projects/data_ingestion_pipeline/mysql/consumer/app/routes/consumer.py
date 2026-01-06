from fastapi import APIRouter, Depends
from app.schemas.country import CountryCreate, CountryResponse
from app.schemas.media_channel import MediaChannelCreate, MediaChannelResponse
from app.core.response import ApiResponse
from app.core.dependencies import get_country_service, get_media_channel_service
from app.services.country_service import CountryService
from app.services.media_channel_service import MediaChannelService

router = APIRouter(prefix="/api/v1/consumer", tags=["Consumer"])

@router.post("/countries", response_model=ApiResponse)
def produce_countries(payload: CountryCreate, service: CountryService = Depends(get_country_service)):
    country = service.create_country(payload)
    return ApiResponse(message="Countries published", data=CountryResponse.model_validate(country))
    # countries = service.produce_countries(payload.countries)
    # return ApiResponse(message="Countries published", data={
    #     "count": len(countries)
    # })

@router.post("/media-channels", response_model=ApiResponse)
def produce_countries(payload: MediaChannelCreate, service: MediaChannelService = Depends(get_media_channel_service)):
    m_channel = service.create_media_channel(payload)
    return ApiResponse(message="Media Channel published", data=MediaChannelResponse.model_validate(m_channel))
# @router.post("/media-channels", response_model=ApiResponse)
# def produce_media_channels(payload: MediaChannelListPayload, service: ProducerService = Depends(get_producer_service)):
#     media_channels = service.produce_media_channels(payload.media_channels)
#     return ApiResponse(message="Media Channels published", data={
#         "count": len(media_channels)
#     })

# @router.post("/companies", response_model=ApiResponse)
# def produce_companies(count: int = Query(10, ge=1, le=1000) , service: ProducerService = Depends(get_producer_service)):
#     service.produce_companies(count)
#     return ApiResponse(message="Companies added to queue", data={
#         "count": count
#     })
