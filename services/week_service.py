import sqlalchemy as sa

from data.week import Week
import data.db_session as db_session


def add_week(week_num, date) -> None:
    new_week = Week(week_number=week_num, date=date)
    session = db_session.create_session()

    try:
        session.add(new_week)
        session.commit()
    finally:
        session.close()
