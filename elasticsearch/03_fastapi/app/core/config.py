from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Elasticsearch Service"

    ELASTICSEARCH_HOST: str = "http://localhost:9200"
    ELASTICSEARCH_USERNAME: str | None = None
    ELASTICSEARCH_PASSWORD: str | None = None

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
