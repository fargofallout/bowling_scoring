import sqlalchemy as sa

from data.currents import Currents
import data.db_session as db_session


def create_current(bowler_id: int, team_id: int, week_id: int, season_id: int) -> None:
    current = Currents(current_bowler=bowler_id, current_team=team_id, current_week=week_id, current_season=season_id)
    session = db_session.create_session()
    try:
        session.add(current)
        session.commit()
    finally:
        session.close()


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


def get_current_season() -> int:
    session = db_session.create_session()
    try:
        current_season = session.execute(sa.select(Currents)).scalar_one()
    finally:
        session.close()
    return current_season.id
