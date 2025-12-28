from fastapi import APIRouter, Depends
from app.schemas.country import CountryListPayload
from app.core.response import ApiResponse
from app.core.dependencies import get_producer_service
from app.services.producer_service import ProducerService

router = APIRouter(prefix="/api/v1/producer", tags=["Producer"])

@router.post("/countries", response_model=ApiResponse)
def produce_countries(payload: CountryListPayload, service: ProducerService = Depends(get_producer_service)):
    countries = service.produce_countries(payload.countries)
    return ApiResponse(message="Countries published", data={
        "count": len(countries)
    })

# def create_user(payload: UserCreate, service: UserService = Depends(get_user_service)):
#     user = service.create_user(payload)
#     return ApiResponse(message="User created", data=UserResponse.model_validate(user))

# @router.get("/", response_model=ApiResponse)
# def list_users(service: UserService = Depends(get_user_service)):
#     users = service.get_all_users()
#     user_list = [UserResponse.model_validate(u) for u in users]
#     return ApiResponse(message="List of users", data=user_list)


# @router.get("/{user_id}", response_model=ApiResponse)
# def get_user_by_id(user_id: int, service: UserService = Depends(get_user_service)):
#     user = service.get_user_by_id(user_id)
#     return ApiResponse(message="User details", data=UserResponse.model_validate(user))





# producer_service = ProducerService()

# @router.post("/users")
# def produce_users(count: int = Query(10, ge=1, le=1000)):
#     producer_service.produce_users(count)
#     return {"entity": "users", "count": count, "status": "PUBLISHED"}

# @router.post("/companies")
# def produce_companies(count: int = Query(10, ge=1, le=1000)):
#     producer_service.produce_companies(count)
#     return {"entity": "companies", "count": count, "status": "PUBLISHED"}

# @router.post("/panelists")
# def produce_panelists(count: int = Query(10, ge=1, le=1000)):
#     producer_service.produce_panelists(count)
#     return {"entity": "panelists", "count": count, "status": "PUBLISHED"}

# @router.post("/products")
# def produce_products(count: int = Query(10, ge=1, le=1000)):
#     producer_service.produce_products(count)
#     return {"entity": "products", "count": count, "status": "PUBLISHED"}
