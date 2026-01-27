from fastapi import APIRouter
from app.models.product import Product
from app.services.product_service import ProductService

router = APIRouter(prefix="/search", tags=["Search"])


@router.post("/product")
async def index_product(product: Product):
    await ProductService.index_product(product.model_dump())
    return {"status": "indexed"}


@router.get("/product")
async def search_product(q: str):
    return await ProductService.search_products(q)
