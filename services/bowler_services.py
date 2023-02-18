import sqlalchemy as sa

from data.bowler import Bowler
import data.db_session as db_session


def add_bowler(bowler_name):
    new_bowler = Bowler(name=bowler_name)
    session = db_session.create_session()
    try:
        session.add(new_bowler)
        session.commit()
    finally:
        session.close()


def get_all_bowlers() -> list:
    session = db_session.create_session()
    try:
        all_bowlers = session.scalars(sa.select(Bowler).order_by(Bowler.id)).all()
    finally:
        session.close()
    return list(all_bowlers)


def bowler_search(search_string) -> list:
    session = db_session.create_session()
    search_string = f"%{search_string}%"
    try:
        bowler_hits = session.scalars(sa.select(Bowler).filter(Bowler.name.like(search_string))).all()
    finally:
        session.close()
    return list(bowler_hits)
