import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from data.modelbase import SqlAlchemyBase


__factory = None

def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("need a database file")

    conn_str = "sqlite:///" + db_file.strip()

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    session: Session = __factory()
    session.expire_on_commit = False
    return session
