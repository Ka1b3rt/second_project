from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    RABBITMQ_URL: str
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(  
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()