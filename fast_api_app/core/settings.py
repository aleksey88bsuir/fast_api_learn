from pydantic_settings import BaseSettings
from pathlib import Path
from pydantic import BaseModel


BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "shop.sqlite3"


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = False


class ConfigApp(BaseSettings):
    api_shop_router: str = "/shop_api"
    db: DbSettings = DbSettings()


config = ConfigApp()
