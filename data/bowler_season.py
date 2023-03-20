from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase


class Bowler_Season(SqlAlchemyBase):
    __tablename__ = "bowler_season"
    id: Mapped[int] = mapped_column(primary_key=True)

    bowler_id: Mapped[int] = mapped_column(ForeignKey("bowler.id"))
    season_id: Mapped[int] = mapped_column(ForeignKey("season.id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    league_id: Mapped[int] = mapped_column(ForeignKey("league.id"))

    # don't think I'm going to need these since none of these will have fields
    # that map back to this class
    # season: Mapped["Season"] = relationship(back_populates="bowler_season")
    # team: Mapped["Team"] = relationship(back_populates="bowler_season")
    # bowler: Mapped["Bowler"] = relationship(back_populates="bowler_season")

