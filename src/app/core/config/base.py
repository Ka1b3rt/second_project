from pydantic_settings import BaseSettings
from app.core.paths import project_paths


class BaseConfig(BaseSettings):
    """Базовый класс для всех конфигураций."""
    
    class Config:
        env_file = project_paths.env_file
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "allow"  