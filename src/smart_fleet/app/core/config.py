from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    project_name: str

    class Config():
        env_file: str = '.env'