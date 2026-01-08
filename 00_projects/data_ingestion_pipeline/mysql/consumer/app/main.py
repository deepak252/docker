from app.kafka.client import KafkaClient
from app.kafka.consumer import KafkaConsumer
from app.kafka.dispatcher import Dispatcher
from app.kafka.topics import COUNTRIES_CREATED

def main():
    consumer = KafkaClient.get_consumer("countries.ingestion.v1")
    dispatcher = Dispatcher()

    KafkaConsumer(consumer, dispatcher).start([
        COUNTRIES_CREATED,
    ])

if __name__ == "__main__":
    main()


# from fastapi import FastAPI
# from app.core.database import Base, engine
# from app.routes import consumer
# from app.core.exceptions import (
#     AppException, 
#     app_exception_handler, 
#     sqlalchemy_exception_handler, 
#     unhandled_exception_handler
# )
# from sqlalchemy.exc import SQLAlchemyError

# # Create DB tables
# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="consumer fastapi")

# @app.get('/')
# def home():
#     return {
#         "status": "ok",
#         "message": "consumer is up"
#     }

# # app.include_router(users.router, prefix="/api")
# app.include_router(consumer.router, prefix="")

# # Custom business error handler
# app.add_exception_handler(AppException, app_exception_handler)
# # SQLAlchemy DB exceptions
# app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
# # Catch-all fallback for ANY other exception
# app.add_exception_handler(Exception, unhandled_exception_handler)
