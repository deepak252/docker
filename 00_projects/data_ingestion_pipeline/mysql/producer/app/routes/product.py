from fastapi import APIRouter, Depends, Query
from app.schemas.product import Product
from app.core.response import ApiResponse
from app.core.dependencies import get_product_service
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Product"])

@router.post("/", response_model=ApiResponse)
def create_product(
    payload: Product,
    service: ProductService = Depends(get_product_service)
):
    service.publish_product(payload)
    return ApiResponse(message="Product published", data=payload)


@router.post("/produce", response_model=ApiResponse)
def produce_products(
    count: int = Query(10, gt=0, le=10000),
    service: ProductService = Depends(get_product_service)
):
    cnt = service.produce_products(count)
    return ApiResponse(
        message="Products published",
        data={"count": cnt}
    )
