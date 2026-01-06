from app.schemas.country import Country
from app.schemas.media_channel import MediaChannel
from app.utils import COUNTRIES, MEDIA_CHANNELS, generate_company
    
class ProducerService:
    def produce_countries(self, countries: list[Country]):
        if len(countries) == 0:
            countries = COUNTRIES
        return countries

    def produce_media_channels(self, media_channels: list[MediaChannel]):
        if len(media_channels) == 0:
            media_channels = MEDIA_CHANNELS
        return media_channels

    def produce_companies(self, count: int):
        for _ in range(count):
            # self.kafka.send("companies.created", generate_company())
            generate_company()

# # app/services/producer_service.py
# from producers.kafka_producer import KafkaProducerClient
# from utils import random_user, random_company, random_panelist, random_product

# class ProducerService:
#     def __init__(self):
#         self.kafka = KafkaProducerClient()

#     def produce_users(self, count: int):
#         for _ in range(count):
#             self.kafka.send("users.created", random_user())

#     def produce_companies(self, count: int):
#         for _ in range(count):
#             self.kafka.send("companies.created", random_company())

#     def produce_panelists(self, count: int):
#         for _ in range(count):
#             self.kafka.send("panelists.created", random_panelist())

#     def produce_products(self, count: int):
#         for _ in range(count):
#             self.kafka.send("products.created", random_product())
