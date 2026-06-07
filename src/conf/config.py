from pathlib import Path

from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Config(BaseSettings):
    DB_URL: str = ""

    JWT_SECRET: str = "your_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_SECONDS: int = 3600

    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


config = Config()
