import sqlalchemy as sa

from data.season import Season
import data.db_session as db_session


def add_season(season):
    new_season = Season(season=season)
    session = db_session.create_session()
    try:
        session.add(new_season)
        session.commit()
    finally:
        session.close()


def get_season_ids():
    return_list = []
    session = db_session.create_session()
    query = sa.select(Season)
    for each_season in session.scalars(query):
        return_list.append([each_season.id, each_season.season])
