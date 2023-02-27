from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase
from data.league import League


class League_Season(SqlAlchemyBase):
    __tablename__ = "league_season"
    id: Mapped[int] = mapped_column(primary_key=True)
    season_id: Mapped[int] = mapped_column(ForeignKey("season.id"))

    league_id: Mapped[int] = mapped_column(ForeignKey("league.id"))
    league: Mapped["League"] = relationship(back_populates="league_seasons")

    def __repr__(self) -> str:
        return f"Season(id={self.id!r})"
