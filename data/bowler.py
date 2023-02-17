from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase


class Bowler(SqlAlchemyBase):
    __tablename__ = "bowler"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
