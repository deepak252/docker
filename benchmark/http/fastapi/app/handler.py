from fastapi import APIRouter, Query, HTTPException
from models import ApiData
from service import WrkloadService

router = APIRouter()
service = WrkloadService()


@router.get("/wrk")
async def wrk(
    e: str = Query("https://example.com"),
    m: str = Query("get"),
    c: int = Query(10),
    d: int = Query(10),
):
    if c <= 0:
        raise HTTPException(status_code=400, detail="invalid connections value")

    if d <= 0:
        raise HTTPException(status_code=400, detail="invalid duration value")

    api_data = ApiData(url=e, method=m)

    result = await service.wrk(
        api_data=api_data,
        connections=c,
        duration=d
    )

    return result