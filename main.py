import argparse
import os
import sqlalchemy as sa

import data.db_session as db_session
from data.team import Team
from services import bowler_services, team_service, utils, season_service

def new_week():
    new_date = utils.get_date()
    print(f"out of that while loop - date: {new_date}")


def setup_db():
    current_dir = os.path.dirname(__file__)
    db_file = os.path.join(current_dir, "db", "db.sqlite")
    db_session.global_init(db_file)


def initial_setup():
    print("creating me and setting me as the current bowler")
    bowler_name = input("my name (first last): ")
    bowler_services.add_bowler(bowler_name)


if __name__ == "__main__":
    setup_db()
    parser = argparse.ArgumentParser()
    parser.add_argument("-ab", "--bowler", help="Name of new bolwer to add.")
    parser.add_argument("-d", "--display", help="Display a week's games.", action="store_true")
    parser.add_argument("-g", "--game", help="Add a game.", action="store_true")
    parser.add_argument("-gb", "--bowlers", help="Get all bowlers", action="store_true")
    parser.add_argument("-i", "--initialize", help="Initial setup.", action="store_true")
    parser.add_argument("-l", "--teams", help="List all teams.", action="store_true")
    parser.add_argument("-n", "--new", help="Begin a new week.", action="store_true")
    parser.add_argument("-r", "--resume", help="Resume data entry for a given week.")
    parser.add_argument("-s", "--season", help="Add a new season.")
    parser.add_argument("-sb", "--searchbowler", help="Bowler name to search for.")
    parser.add_argument("-t", "--team", help="Name of new team to add.")
    parser.add_argument("-ts", "--teamseason", help="Add a season for a team.", action="store_true")

    args = parser.parse_args()

    if args.new:
        new_week()
    elif args.display:
        print("doing stuff with a previous week")
    elif args.bowler:
        bowler_services.add_bowler(args.bowler)
    elif args.team:
        team_service.add_team(args.team)
    elif args.resume:
        print("resuming data entry")
    elif args.teams:
        team_list = team_service.get_teams()
        print("Number\tTeam name")
        for each_team in team_list:
            print(f"{each_team.id}\t{each_team.name}")
    elif args.game:
        print("adding a game")
    elif args.teamseason:
        print("adding a team season")
    elif args.season:
        season_service.add_season(args.season)
    elif args.initialize:
        initial_setup()
    elif args.bowlers:
        all_bowlers = bowler_services.get_all_bowlers()
    elif args.searchbowler:
        bowler_hits = bowler_services.bowler_search(args.searchbowler)
        for each_hit in bowler_hits:
            print(f"id: {each_hit.id}, name: {each_hit.name}")

