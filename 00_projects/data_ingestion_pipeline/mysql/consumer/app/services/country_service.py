from app.repositories.country_repository import CountryRepository
from app.schemas.country import CountryCreate
from app.models.country import Country

class CountryService:
    repo: CountryRepository

    def __init__(self, repo: CountryRepository):
        self.repo = repo

    def create_country(self, payload: CountryCreate):
        country = Country(name=payload.name, iso_code=payload.iso_code)
        return self.repo.create(country)
    
    def get_all_countries(self):
        return self.repo.get_all()
    
        
    