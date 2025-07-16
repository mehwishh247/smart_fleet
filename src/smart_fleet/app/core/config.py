from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    project_name: str
    frontend_origins: List[str]
    db_name: str

    class Config():
        env_file: str = '.env'