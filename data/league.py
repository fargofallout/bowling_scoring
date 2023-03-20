from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from data.modelbase import SqlAlchemyBase


class League(SqlAlchemyBase):
    __tablename__ = "league"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()


    def __repr__(self) -> str:
        return f"League(id={self.id!r}, name={self.name!r})"
