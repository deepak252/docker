from sqlalchemy.orm import Session
from app.models.country import Country

class CountryRepository:
    db: Session
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, country: Country):
        self.db.add(country)
        self.db.commit()
        self.db.refresh(country)
        return country
    
    def get_all(self):
        return self.db.query(Country).all()
    