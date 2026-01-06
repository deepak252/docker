from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
# from app.repositories.user_repository import UserRepository
from app.repositories.company_repository import CompanyRepository
from app.repositories.country_repository import CountryRepository
from app.repositories.media_channel_repository import MediaChannelRepository
# from app.services.consumer_service import ConsumerService
from app.services.company_service import CompanyService
from app.services.country_service import CountryService
from app.services.media_channel_service import MediaChannelService


def get_company_service(db: Session = Depends(get_db)):
    repo = CompanyRepository(db)
    return CompanyService(repo)

def get_country_service(db: Session = Depends(get_db)):
    repo = CountryRepository(db)
    return CountryService(repo)

def get_media_channel_service(db: Session = Depends(get_db)):
    repo = MediaChannelRepository(db)
    return MediaChannelService(repo)