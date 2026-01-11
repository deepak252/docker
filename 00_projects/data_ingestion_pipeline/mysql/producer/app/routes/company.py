from fastapi import APIRouter, Depends, Query
from app.schemas.company import Company
from app.core.response import ApiResponse
from app.core.dependencies import  get_company_service
from app.services.company_service import CompanyService

router = APIRouter(prefix="/companies", tags=["Company"])

@router.post("/", response_model=ApiResponse)
def create_company(payload: Company, service: CompanyService = Depends(get_company_service)):
    service.publish_company(payload)
    return ApiResponse(message="Company published", data=payload)

@router.post("/produce", response_model=ApiResponse)
def produce_companies(
    count: int = Query(10, gt=0, le=10000, description="Number of companies to produce"),
    service: CompanyService = Depends(get_company_service)
):
    cnt = service.produce_companies(count)
    return ApiResponse(message="Companies published", data={
        "count": cnt
    })