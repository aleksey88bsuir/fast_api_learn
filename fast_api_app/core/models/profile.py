from typing import TYPE_CHECKING

from .base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .mixins import UserRelationMixin


if TYPE_CHECKING:
    from .user import User


class Profile(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "profile"
    first_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))
    bio: Mapped[str | None]
