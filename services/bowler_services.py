from data.bowler import Bowler
import data.db_session as db_session


def add_bowler(bowler_name):
    new_bowler = Bowler(name=bowler_name)
    session = db_session.create_session()
    try:
        session.add(new_bowler)
        session.commit()
    finally:
        session.close()

