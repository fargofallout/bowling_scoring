from data.team import Team
import data.db_session as db_session


def add_team(team_name: str) -> None:

    new_team = Team(name=team_name)
    session = db_session.create_session()

    try:
        session.add(new_team)
        session.commit()
    finally:
        session.close()
