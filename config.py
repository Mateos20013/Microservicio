from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "User Service"
    admin_email: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
