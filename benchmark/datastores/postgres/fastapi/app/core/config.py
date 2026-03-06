from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # DATABASE_URL:str = "postgresql://root:root@localhost:5432/testdb"
    DATABASE_URL:str = "postgresql://root:root@localhost:5432/testdb"
    # Pydantic configuration class (nested class)
    class Config: 
        env_file = ".env"
     
    
# SINGLETON PATTERN (Configuration Singleton)
# Created one single instance of Settings, imported and used everywhere in the app.
settings = Settings()