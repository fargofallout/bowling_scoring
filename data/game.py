import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from data.modelbase import SqlAlchemyBase
from data.bowler import Bowler
from data.team import Team


class Game(SqlAlchemyBase):
    __tablename__ = "game"
    id: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[int] = mapped_column()
    date: Mapped[datetime.datetime] = mapped_column()
    week: Mapped[int] = mapped_column()
    season: Mapped[str] = mapped_column()

    bowler_id: Mapped[int] = mapped_column(ForeignKey("bowler.id"))
    bowler: Mapped["Bowler"] = relationship(back_populates="game")

    opponent_game_id: Mapped[int] = mapped_column(ForeignKey("game.id"))

    team_id = Mapped[int] = mapped_column(ForeignKey("team.id"))
    team: Mapped["Team"] = relationship(back_populates="game")
