import sqlalchemy as sa

from data.currents import Currents
import data.db_session as db_session


def set_current_bowler(bowler_id: int) -> None:
    session = db_session.create_session()
    try:
        the_current = session.execute(sa.select(Currents)).scalar_one()
        the_current.current_bowler = bowler_id
        session.commit()
    finally:
        session.close()


def get_current_bowler() -> int:
    session = db_session.create_session()
    try:
        current_user = session.execute(sa.select(Currents)).scalar_one()
    finally:
        session.close()

    return current_user.id
