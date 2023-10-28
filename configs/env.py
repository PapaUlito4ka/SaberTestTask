import os

from pydantic_settings import BaseSettings


def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.prod" if runtime_env else ".env.dev"


class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    DEBUG_MODE: bool

    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


def get_environment_variables():
    return EnvironmentSettings()
