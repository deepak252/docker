from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.dependencies import get_user_service
from app.core.response import ApiResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=ApiResponse, status_code=201)
def create_user(payload: UserCreate, service: UserService = Depends(get_user_service)):
    user = service.create_user(payload)
    return ApiResponse(message="User created", data=UserResponse.model_validate(user))


@router.get("/", response_model=ApiResponse)
def list_users(service: UserService = Depends(get_user_service)):
    users = service.get_all_users()
    user_list = [UserResponse.model_validate(u) for u in users]
    return ApiResponse(message="List of users", data=user_list)


@router.get("/{user_id}", response_model=ApiResponse)
def get_user_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user_by_id(user_id)
    return ApiResponse(message="User details", data=UserResponse.model_validate(user))
