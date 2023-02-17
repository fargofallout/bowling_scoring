from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.modelbase import SqlAlchemyBase


class Team(SqlAlchemyBase):
    __tablename__ = "team"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
