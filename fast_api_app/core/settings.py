from pydantic_settings import BaseSettings
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
print(BASE_DIR)


class ConfigApp(BaseSettings):
    api_shop_router: str = "/shop_api"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/shop.sqlite3"
    db_echo: bool = True


config = ConfigApp()
