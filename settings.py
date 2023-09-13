import os

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'),
                                      env_file_encoding='utf-8')

    APP_NAME: str
    POSTGRES_DB_URL: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    ACCESSTOKEN_SECRET_KEY: str
    REFRESHTOKEN_SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    MAX_MEDIA_SIZE: int
    ALLOWED_MEDIA_TYPES: str

    SMTP_USER: str
    SMTP_PASSWORD: str
    SMTP_HOST: str
    SMTP_PORT: int

    @model_validator(mode="after")
    def check_passwords_match(self) -> 'Settings':
        acc = self.ACCESSTOKEN_SECRET_KEY
        ref = self.REFRESHTOKEN_SECRET_KEY
        if acc is None and ref is None or acc == ref:
            raise ValueError('Secret Key for Access- and Refreshtoken cant be the same!')
        return self


settings = Settings()
