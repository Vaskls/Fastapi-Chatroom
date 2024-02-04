from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    
    jwt_secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    jwt_refresh_secret_key: str

    class Config:
        env_file = ".env"


settings = Settings()