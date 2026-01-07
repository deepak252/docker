from fastapi import APIRouter, Depends
from app.schemas.country import Country
from app.core.response import ApiResponse
from app.core.dependencies import  get_country_service
from app.services.country_service import CountryService
from typing import Optional
router = APIRouter(prefix="/countries", tags=["Country"])

@router.post("/", response_model=ApiResponse)
def create_country(payload: Optional[Country], service: CountryService = Depends(get_country_service)):
    service.publish_country(payload)
    return ApiResponse(message="Country published", data=payload)

@router.post("/produce", response_model=ApiResponse)
def produce_countries(service: CountryService = Depends(get_country_service)):
    cnt = service.produce_countries()
    return ApiResponse(message="Countries published", data={
        "count": cnt
    })