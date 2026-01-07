from app.services.producer_service import ProducerService
from app.services.country_service import CountryService

def get_producer_service():
    return ProducerService()

def get_country_service():
    return CountryService()