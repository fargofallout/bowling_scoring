from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase
from data.season import Season
from data.team import Team


class Team_Season(SqlAlchemyBase):
    __tablename__ = "team_season"
    id: Mapped[int] = mapped_column(primary_key=True)

    team_id: Mapped[int] = mapped_column(ForeignKey("bowler.id"))
    team: Mapped["Team"] = relationship(back_populates="team", lazy="selectin")

    season_id: Mapped[int] = mapped_column(ForeignKey("season.id"))
    season: Mapped["Season"] = relationship(back_populates="season", lazy="selectin")
