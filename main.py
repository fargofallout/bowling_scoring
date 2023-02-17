import argparse
import os
import sqlalchemy as sa
import datetime
import regex

import data.db_session as db_session
from data.team import Team
from services import bowler_services


def new_week():
    date_regex_1 = regex.compile(r"(\d\d\d\d)(\.|-)(\d+)(\.|-)(\d+)")
    date_regex_2 = regex.compile(r"(\d+)/(\d+)/(\d\d\d\d)")
    print("Enter the date of the games, or enter 'today' to use today")
    date = input("date: ")
    date = date.lower().strip()
    valid_input = False
    date_as_datetime = ""
    while not valid_input:
        if date == "today" or date == "t":
            date_as_datetime = datetime.datetime.now()
            valid_input = True

        elif date_regex_1.search(date):
            date_match = date_regex_1.search(date)
            year = int(date_match.group(1))
            month = int(date_match.group(3))
            day = int(date_match.group(5))
            date_as_datetime = datetime.date(year, month, day)
            try:
                date_as_datetime = datetime.date(year, month, day)
            except ValueError as e:
                print("Not a valid date format. Please try again.")
                date = input("date: ")
                continue
            valid_input = True

        elif date_regex_2.search(date):
            date_match = date_regex_2.search(date)
            year = int(date_match.group(3))
            month = int(date_match.group(1))
            day = int(date_match.group(2))
            try:
                date_as_datetime = datetime.date(year, month, day)
            except ValueError as e:
                print("Not a valid date format. Please try again.")
                date = input("date: ")
                continue
            valid_input = True
        else:
            print("Not a valid date format. Please try again.")
            date = input("date: ")
            valid_input = False

    print(f"out of that while loop - date: {date_as_datetime}")

def add_team(team_name):
    new_team = Team(name=team_name)
    session = db_session.create_session()
    try:
        session.add(new_team)
        session.commit()
    finally:
        session.close()


def get_teams():
    session = db_session.create_session()
    query = sa.select(Team)
    for each_team in session.scalars(query):
        print(f"{each_team.id}:  {each_team.name}")


def setup_db():
    current_dir = os.path.dirname(__file__)
    db_file = os.path.join(current_dir, "db", "db.sqlite")
    db_session.global_init(db_file)


if __name__ == "__main__":
    setup_db()
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--new", help="Begin a new week.", action="store_true")
    parser.add_argument("-b", "--bowler", help="Name of new bolwer to add.")
    parser.add_argument("-t", "--team", help="Name of new team to add.")
    parser.add_argument("-r", "--resume", help="Resume data entry for a given week.")
    parser.add_argument("-d", "--display", help="Display a week's games.", action="store_true")
    parser.add_argument("-l", "--teams", help="List all teams.", action="store_true")
    parser.add_argument("-g", "--game", help="Add a game.", action="store_true")
    parser.add_argument("-ts", "--teamseason", help="Add a season for a team.", action="store_true")
    parser.add_argument("-s", "--season", help="Add a new season.", action="store_true")

    args = parser.parse_args()

    if args.new:
        new_week()
    elif args.display:
        print("doing stuff with a previous week")
    elif args.bowler:
        bowler_services.add_bowler(args.bowler)
    elif args.team:
        add_team(args.team)
    elif args.resume:
        print("resuming data entry")
    elif args.teams:
        get_teams()
    elif args.game:
        print("adding a game")
    elif args.teamseason:
        print("adding a team season")
    elif args.season:
        print("adding a season")

