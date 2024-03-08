from .base import Base

from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class Order(Base):
    promocode: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
    )
    total_price: Mapped[int]
