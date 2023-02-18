import sqlalchemy as sa

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


def get_teams() -> list:
    session = db_session.create_session()
    try:
        all_teams = session.scalars(sa.select(Team)).all()
    finally:
        session.close()
    return all_teams

    # this creates a list of items of type <data.team.Team object
    # it can be iterated over and you can pull out each_item.id or whatever,
    # but they are not plain Team objects
    # try:
    #     statement = sa.select(Team)
    #     all_teams = session.scalars(statement).all()
    #     for each_item in all_teams:
    #         print(each_item)
    # finally:
    #     session.close()

    # this creates a list of tuples -> [(team.id, team.name)]
    # session = db_session.create_session()
    # try:
    #     statement = sa.select(Team.id, Team.name)
    #     rows = session.execute(statement).all()
    # finally:
    #     session.close()

