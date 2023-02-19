import sqlalchemy as sa
from typing import Optional

from data.week import Week
import data.db_session as db_session


def add_week(week_num, date) -> Optional[Week]:
    new_week = Week(week_number=week_num, date=date)
    session = db_session.create_session()

    try:
        session.add(new_week)
        session.commit()
    finally:
        session.close()

    return new_week


def add_all_weeks(starting_date, num_weeks) -> None:
    # CONTINUE HERE: need to create all dates for a given season
    pass
