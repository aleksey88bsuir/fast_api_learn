from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from fast_api_app.core.settings import config


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocomit=False,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(
    url=config.db_url,
    echo=config.db_echo,
)
