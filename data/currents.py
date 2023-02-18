from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase


class Currents(SqlAlchemyBase):
    __tablename__ = "currents"
    id: Mapped[int] = mapped_column(primary_key=True)

    current_bowler: Mapped[int] = mapped_column(ForeignKey("bowler.id"))
    current_team: Mapped[int] = mapped_column(ForeignKey("team.id"))
    curent_week: Mapped[int] = mapped_column(ForeignKey("week.id"))
    current_season: Mapped[int] = mapped_column(ForeignKey("season.id"))

    # I don't think I need the relationships since this is a helper table and no reference
    # to this table exists on the others?
    # season: Mapped["Season"] = relationship(back_populates="currents")
    # bowler: Mapped["Bowler"] = relationship(back_populates="currents")

