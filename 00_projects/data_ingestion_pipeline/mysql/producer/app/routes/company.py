from fastapi import APIRouter, Depends, Query
from app.schemas.company import Company
from app.core.response import ApiResponse
from app.core.dependencies import  get_company_service
from app.services.company_service import CompanyService
import time

router = APIRouter(prefix="/companies", tags=["Company"])

@router.post("/", response_model=ApiResponse)
def create_company(payload: Company, service: CompanyService = Depends(get_company_service)):
    service.publish_company(payload)
    return ApiResponse(message="Company published", data=payload)

@router.post("/produce", response_model=ApiResponse)
async def produce_companies(
    count: int = Query(10, gt=0, le=1000000, description="Number of companies to produce"),
    service: CompanyService = Depends(get_company_service)
):
    print("Request Recieved")
    start_time = time.perf_counter()
    cnt = service.produce_companies(count)
    elapsed_time = time.perf_counter() - start_time
    return ApiResponse(message="Companies published", data={
        "count": cnt,
        "time_taken_seconds": round(elapsed_time, 6)
    })