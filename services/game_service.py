import datetime
from typing import Optional

from data.game import Game
import data.db_session as db_session


def add_game(score: int,
             week: int,
             season: str,
             bowler_id: int,
             team_id: int,
             game_date: Optional[datetime] = None) -> Optional[Game]:

    if not game_date:
        game_date = datetime.datetime.now()

    new_game = Game(score=score, week=week, season=season, bowler_id=bowler_id, team_id=team_id, date=game_date)
    session = db_session.create_session()

    try:
        session.add(new_game)
        session.commit()
    finally:
        session.close()

    return new_game
