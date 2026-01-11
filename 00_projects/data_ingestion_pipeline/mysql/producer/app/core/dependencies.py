from app.services.country_service import CountryService
from app.services.company_service import CompanyService
from app.services.media_channel_service import MediaChannelService
from app.services.product_service import ProductService
from app.services.product_media_service import ProductMediaService

def get_country_service():
    return CountryService()

def get_media_channel_service():
    return MediaChannelService()

def get_company_service():
    return CompanyService()

def get_product_service():
    return ProductService()

def get_product_media_service():
    return ProductMediaService()