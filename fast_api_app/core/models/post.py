from .base import Base
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Post(Base):
    title: Mapped[str] = mapped_column(String(50), unique=False)
    body: Mapped[str] = mapped_column(Text,
                                      default='',
                                      server_default=''
                                      )

