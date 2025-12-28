from app.schemas.country import Country
from app.utils import COUNTRIES
class ProducerService:
    def produce_countries(self, countries: list[Country]):
        if len(countries) == 0:
            countries = COUNTRIES
            
        return countries

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
