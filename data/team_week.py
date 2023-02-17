from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase
from data.season import Season
from data.team import Team


class Team_Week(SqlAlchemyBase):
    __tablename__ = "team_week"
    id: Mapped[int]  = mapped_column(primary_key=True)

    season_id: Mapped[int] = mapped_column(ForeignKey("season.id"))
    season: Mapped["Season"] = relationship(back_populates="team_week")

    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    team: Mapped["Team"] = relationship(back_populates="team_week")
