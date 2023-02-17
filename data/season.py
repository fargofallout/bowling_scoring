from sqlalchemy.orm import Mapped, mapped_column

from data.modelbase import SqlAlchemyBase


class Season(SqlAlchemyBase):
    __tablename__ = "season"
    id: Mapped[int] = mapped_column(primary_key=True)
    season: Mapped[str] = mapped_column()
