from pydantic_settings import BaseSettings


class ConfigApp(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./shop.db"
    db_echo: bool = True


config = ConfigApp()
