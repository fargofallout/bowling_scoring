from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from data.modelbase import SqlAlchemyBase


class Week(SqlAlchemyBase):
    __tablename__ = "week"
    id: Mapped[int] = mapped_column(primary_key=True)
    week_number: Mapped[str] = mapped_column()
    date: Mapped[datetime] = mapped_column()
