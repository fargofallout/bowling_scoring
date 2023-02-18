from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase


class Team_Week(SqlAlchemyBase):
    __tablename__ = "team_week"
    id: Mapped[int]  = mapped_column(primary_key=True)

    season_id: Mapped[int] = mapped_column(ForeignKey("season.id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))

    # more relationships I don't think I'll need
    # team: Mapped["Team"] = relationship(back_populates="team_week")
    # season: Mapped["Season"] = relationship(back_populates="team_week")

