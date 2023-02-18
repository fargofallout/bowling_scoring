from sqlalchemy.orm import Mapped, mapped_column

from data.modelbase import SqlAlchemyBase


class Bowler(SqlAlchemyBase):
    __tablename__ = "bowler"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
