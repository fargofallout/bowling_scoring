import sqlalchemy as sa
import regex
from typing import Optional

from data.season import Season
import data.db_session as db_session


def add_season(season) -> Optional[Season]:
    season_regex = regex.compile(r"^\d\d\d\d-\d\d$")
    if not season_regex.search(season):
        return

    new_season = Season(season=season)
    session = db_session.create_session()
    try:
        session.add(new_season)
        session.commit()
    finally:
        session.close()

    return new_season


def get_season_ids() -> list[int]:
    return_list = []
    session = db_session.create_session()
    try:
        query = session.scalars(sa.select(Season)).all()
        for each_season in query:
            return_list.append(each_season.id)
    finally:
        session.close()
    return return_list


def search_for_season(season_string) -> Optional[Season]:
    session = db_session.create_session()
    try:
        season = session.get(Season, season_string)
        print(f"what the hell? {type(season)}")
        print(season)
    finally:
        session.close()

    if season:
        return season
    else:
        return
