from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str = "mysql+pymysql://admin:admin@localhost:3306/productsdb"
    KAFKA_BOOTSTRAP: str = "localhost:9092"
    KAFKA_GROUP_ID: str = "producer.service.v1"
    # Pydantic configuration class (nested class)
    class Config: 
        env_file = ".env"
     
    
# SINGLETON PATTERN (Configuration Singleton)
# Created one single instance of Settings, imported and used everywhere in the app.
settings = Settings()