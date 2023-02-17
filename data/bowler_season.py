from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.bowler import Bowler
from data.team import Team
from data.season import Season
from data.modelbase import SqlAlchemyBase


class Bowler_Season(SqlAlchemyBase):
    __tablename__ = "bowler_season"
    id: Mapped[int] = mapped_column(primary_key=True)

    season_id: Mapped[int] = mapped_column(ForeignKey("season.id"))
    season: Mapped["Season"] = relationship(back_populates="bowler_season")

    bowler_id: Mapped[int] = mapped_column(ForeignKey("bowler.id"))
    bowler: Mapped["Bowler"] = relationship(back_populates="bowler_season")

    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    team: Mapped["Team"] = relationship(back_populates="bowler_season")
