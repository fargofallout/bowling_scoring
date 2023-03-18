from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase
from data.league import League
# import data.league as league


class League_Season(SqlAlchemyBase):
    __tablename__ = "league_season"
    id: Mapped[int] = mapped_column(primary_key=True)
    season_id: Mapped[int] = mapped_column(ForeignKey("season.id"))

    league_id: Mapped[int] = mapped_column(ForeignKey("league.id"))
    league: Mapped["League"] = relationship(back_populates="league_seasons", lazy="selectin")
    # NOTE: using lazy="selectin" above makes the query grab all related objects, which, in a large application,
    # could cause problems. I doubt it would be a problem in this particular application, so I may want to use
    # it everywhere?

    def __repr__(self) -> str:
        return f"Season(id={self.id!r})"
