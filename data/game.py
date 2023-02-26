import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from data.modelbase import SqlAlchemyBase


class Game(SqlAlchemyBase):
    __tablename__ = "game"
    id: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[int] = mapped_column()
    date: Mapped[datetime.datetime] = mapped_column()
    week: Mapped[int] = mapped_column()
    season: Mapped[str] = mapped_column()

    bowler_id: Mapped[int] = mapped_column(ForeignKey("bowler.id"))
    opponent_game_id: Mapped[int] = mapped_column(ForeignKey("game.id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))

    # not sure if this will require relationships? probably not
    # team: Mapped["Team"] = relationship(back_populates="game")
    # bowler: Mapped["Bowler"] = relationship(back_populates="game")

    def __repr__(self) -> str:
        return f"Game(id={self.id!r}, score={self.score!r}, date={self.date!r}, week={self.week!r}, season={self.season!r})"
