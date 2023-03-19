import sqlalchemy as sa
from typing import Optional

from data.team_season import Team_Season
import data.db_session as db_session


def add_team_season(team_id: int, season_id: int) -> Optional[Team_Season]:
    new_team_season = Team_Season(team_id=team_id, season_id=season_id)
    session = db_session.create_session()

    try:
        session.add(new_team_season)
        session.commit()
    finally:
        session.close()

    return new_team_season


def get_team_seasons_from_team_id(team_id: int) -> list:
    session = db_session.create_session()
    try:
        team_season_search = session.scalars(sa.select(Team_Season).filter(Team_Season.team_id == team_id)).all()
    finally:
        session.close()
    return list(team_season_search)
