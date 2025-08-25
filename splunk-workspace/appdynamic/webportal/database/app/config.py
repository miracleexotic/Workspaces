from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    db_ipaddress: str
    db_port: int
    db_database: str
    db_username: str
    db_password: str
    db_uri: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "AppDynamics WebPortal"
    log_level: str = "DEBUG"


settings = Settings()  # type: ignore

if __name__ == "__main__":
    print(settings)
