from sqlalchemy.orm import Session
from app.models.company import Company

class CompanyRepository:
    db: Session
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, company: Company):
        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)
        return company
    
    def get_all(self):
        return self.db.query(Company).all()
    
# from sqlalchemy.orm import Session
# from app.models.user import User

# class CompanyRepository:
#     db: Session
#     def __init__(self, db: Session):
#         self.db = db
    
#     def create(self, user: User):
#         self.db.add(user)
#         self.db.commit()
#         self.db.refresh(user)
#         return user
    
#     def get_all(self):
#         return self.db.query(User).all()
    
#     def get_by_email(self, email: str):
#         return self.db.query(User).filter(User.email == email).first()
    
#     def get_by_id(self, id: int):
#         return self.db.query(User).filter(User.id == id).first()