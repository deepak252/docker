from fastapi import APIRouter, Depends, Query, HTTPException
from app.schemas.product_media import ProductMedia
from app.core.response import ApiResponse
from app.core.dependencies import get_product_media_service
from app.services.product_media_service import ProductMediaService

router = APIRouter(prefix="/product-media", tags=["Product Media"])

@router.post("/", response_model=ApiResponse)
def create_product_media(
    payload: ProductMedia,
    service: ProductMediaService = Depends(get_product_media_service)
):
    service.publish_product_media(payload)
    return ApiResponse(message="Product media published", data=payload)


@router.post("/produce", response_model=ApiResponse)
def produce_product_media(
    # count: int = Query(10, gt=0, le=10000),
    start_id: int = Query(..., gt=0),
    end_id: int = Query(..., gt=0),
    service: ProductMediaService = Depends(get_product_media_service)
):
    # cnt = service.produce_product_media(count)
    try:
        cnt = service.produce_product_media(start_id, end_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return ApiResponse(
        message="Product media published",
        data={"count": cnt}
    )
