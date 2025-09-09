from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "root"
    DB_PASS: str = "Nihal@123"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306 
    DB_NAME: str = "fastapi_todo"
    JWT_SECRET: str = "supersecretjwt"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"

settings = Settings()
