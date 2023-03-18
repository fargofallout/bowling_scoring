from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from data.modelbase import SqlAlchemyBase
# from data.league_season import League_Season


class League(SqlAlchemyBase):
    __tablename__ = "league"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    league_seasons: Mapped[List["League_Season"]] = relationship(back_populates="league")


    def __repr__(self) -> str:
        return f"League(id={self.id!r}, name={self.name!r})"
