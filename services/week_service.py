import sqlalchemy as sa
from typing import Optional
import datetime

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


def add_all_weeks(starting_date: datetime, num_weeks: int) -> None:
    session = db_session.create_session()
    try:
        for num in range(num_weeks):
            if num != 0:
                starting_date = starting_date + datetime.timedelta(days=7)
            new_week = Week(week_number=num+1, date=starting_date)
            session.add(new_week)
        session.commit()
    finally:
        session.close()


def get_week(week_num: int) -> Optional[int]:
    session = db_session.create_session()
    try:
        week_search = session.scalars(sa.select(Week).filter(Week.week_number == week_num)).one_or_none()
    finally:
        session.close()

    if week_search:
        return week_search.id
    else:
        return
