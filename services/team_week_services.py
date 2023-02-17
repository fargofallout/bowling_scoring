from data.team_week import Team_Week
import data.db_session as db_session


def create_team_week(season_id, team_id):
    new_week = Team_Week(season_id=season_id, team_id=team_id)
    session = db_session.create_session()
    try:
        session.add(new_week)
        session.commit()
    finally:
        session.close()
