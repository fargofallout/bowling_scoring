import sqlalchemy as sa
from typing import Optional

from data.league import League
import data.db_session as db_session


def add_league(league_name: str) -> Optional[League]:
    new_league = League(name=league_name)
    session = db_session.create_session()
    try:
        session.add(new_league)
        session.commit()
    finally:
        session.close()

    return new_league


def get_all_leagues() -> list:
    session = db_session.create_session()
    try:
        all_leagues = session.scalars(sa.select(League).order_by(League.id)).all()
    finally:
        session.close()
    return list(all_leagues)


def get_single_league_from_id(league_id: int) -> Optional[League]:
    session = db_session.create_session()
    try:
        league = session.get(League, league_id)
    finally:
        session.close()
    return league


def search_for_league(league_name: str) -> list:
    session = db_session.create_session()
    try:
        league_hit = session.scalars(sa.select(League).filter(League.name.like(league_name))).all()
    finally:
        session.close()
    return league_hit

