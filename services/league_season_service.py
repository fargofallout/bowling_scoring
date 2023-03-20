from typing import Optional

from data.league_season import League_Season
import data.db_session as db_session


def add_league_season(season_id: int, league_id: int) -> Optional[League_Season]:
    session = db_session.create_session()
    new_league_season = League_Season(season_id=season_id, league_id=league_id)
    try:
        session.add(new_league_season)
        session.commit()
    finally:
        session.close()
    return new_league_season


def get_league_season_from_id(league_season_id: int) -> Optional[League_Season]:
    session = db_session.create_session()
    try:
        league_season_hit = session.get(League_Season, league_season_id)
    finally:
        session.close()
    return league_season_hit
