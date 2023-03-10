from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase


class Team_Season(SqlAlchemyBase):
    __tablename__ = "team_season"
    id: Mapped[int] = mapped_column(primary_key=True)
    season: Mapped[str] = mapped_column()

    team_id: Mapped[int] = mapped_column(ForeignKey("bowler.id"))

    # don't think I'll need this relationship
    # team: Mapped["Team"] = relationship(back_populates="bowler_season")
