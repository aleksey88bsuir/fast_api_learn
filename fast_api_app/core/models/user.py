from typing import TYPE_CHECKING

from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .post import Post


class User(Base):
    name: Mapped[str] = mapped_column(String(30), unique=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
