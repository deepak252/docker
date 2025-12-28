from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User
from app.core.exceptions import AppException

class UserService:
    repo: UserRepository

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, payload: UserCreate):
        existing = self.repo.get_by_email(payload.email)

        if existing:
            raise AppException("Email already exists", 409)
        
        user = User(name = payload.name, email = payload.email)
        return self.repo.create(user)
    
    def get_all_users(self):
        return self.repo.get_all()
    
    def get_user_by_id(self, id: int):
        user = self.repo.get_by_id(id)
        if not user:
            raise AppException("User not found", 404)
        return user
        
    