from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Calculator"

settings = Settings()



