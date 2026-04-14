from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    STRIPE_SECRET_KEY_SANDBOX: str
    AIRALO_API_KEY: str
    AIRALO_API_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()