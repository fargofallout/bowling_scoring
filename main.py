import argparse
import os
import sqlalchemy as sa
import datetime

import data.db_session as db_session
from data.team import Team
from services import bowler_service, team_service, utils, season_service, currents_service, week_service, league_season_service, league_service

def new_week():
    current_season = currents_service.get_current_season()
    all_weeks = week_service.get_all_weeks(current_season)
    selected_week = utils.display_weeks(all_weeks)

    all_teams = team_service.get_teams()
    selected_team = utils.display_teams(all_teams)


def add_week():
    week_number = utils.get_week_num()
    date = utils.get_date()
    week_service.add_week(week_number, date)


def setup_db():
    current_dir = os.path.dirname(__file__)
    db_file = os.path.join(current_dir, "db", "db.sqlite")
    db_session.global_init(db_file)


def initial_setup():
    print("Setup for the rest of 2022-23 - if bowling in 2023-24, need to create that information differently")
    # TODO: change this so I get the values from the command prompt so I can reuse this in future seasons
    # create season
    season_string = "2022-23"
    the_season = season_service.add_season(season_string)

    # create all weeks for season
    num_weeks = 32
    starting_date = datetime.datetime(2022, 9, 6)
    week_service.add_all_weeks(starting_date, num_weeks, the_season.id)

    # create bowler
    bowler_name = "Mike Vacha"
    the_bowler = bowler_service.add_bowler(bowler_name)

    # create team
    team_name = "Big Ern"
    the_team = team_service.add_team(team_name)

    # get current week_id and set values for currents
    current_week = 25
    week_id = week_service.get_week(current_week)
    currents_service.create_current(the_bowler.id, the_team.id, week_id, the_season.id)


def new_league():
    league_id = utils.create_league()
    print(f"this this the id? {league_id}")


if __name__ == "__main__":
    setup_db()

    parser = argparse.ArgumentParser()
    # parser.add_argument("-ab", "--bowler", help="Name of new bolwer to add.")
    # parser.add_argument("-aaw", "--add_all_weeks", help="Input season in format '2022-23' - create all weeks for season")
    # parser.add_argument("-asw", "--add_single_week", help="Add a week", action="store_true")
    parser.add_argument("-cl", "--create_league", help="Set up a new league", action="store_true")
    # parser.add_argument("-d", "--display", help="Display a week's games.", action="store_true")
    # parser.add_argument("-g", "--game", help="Add a game.", action="store_true")
    # parser.add_argument("-gab", "--bowlers", help="Get all bowlers", action="store_true")
    parser.add_argument("-gsb", "--getsinglebowler", help="Exact bowler name to search for.")
    parser.add_argument("-i", "--initialize", help="Initial setup.", action="store_true")
    # parser.add_argument("-l", "--teams", help="List all teams.", action="store_true")
    parser.add_argument("-n", "--new", help="Begin a new week.", action="store_true")
    # parser.add_argument("-r", "--resume", help="Resume data entry for a given week.")
    # parser.add_argument("-s", "--season", help="Add a new season.")
    # parser.add_argument("-sb", "--searchbowler", help="Bowler name to search for.")
    # parser.add_argument("-t", "--team", help="Name of new team to add.")
    # parser.add_argument("-ts", "--teamseason", help="Add a season for a team.", action="store_true")
    parser.add_argument("-tmp", "--tempfunc", action="store_true")
    #
    args = parser.parse_args()
    #
    if args.new:
        new_week()
    elif args.tempfunc:
        print("yup")
        # this creates two leagues, a season, and two league seasons
        # first_league = league_service.add_league("the first league")
        # second_league = league_service.add_league("the second league")
        # season_id = season_service.add_season("2022-23")
        # league_season_service.add_league_season(season_id.id, first_league.id)
        # league_season_service.add_league_season(season_id.id, second_league.id)

        # this tests the relationship on the league season to see how it works
        # a_league_season = league_season_service.get_league_season_from_id(2)
        # print(f"league season id: {a_league_season.id}")
        # print(f"league season season id: {a_league_season.season_id}")
        # print(f"league season league id: {a_league_season.league_id}")
        # print(f"league season league? {a_league_season.league}")
        # print(f"league season league name? {a_league_season.league.name}")

    elif args.create_league:
        new_league()
    # elif args.display:
    #     print("doing stuff with a previous week")
    # elif args.bowler:
    #     bowler_services.add_bowler(args.bowler)
    # elif args.team:
    #     team_service.add_team(args.team)
    # elif args.resume:
    #     print("resuming data entry")
    # elif args.teams:
    #     team_list = team_service.get_teams()
    #     print("Number\tTeam name")
    #     for each_team in team_list:
    #         print(f"{each_team.id}\t{each_team.name}")
    # elif args.game:
    #     print("adding a game")
    # elif args.teamseason:
    #     print("adding a team season")
    # elif args.season:
    #     season_service.add_season(args.season)
    elif args.initialize:
        initial_setup()
    # elif args.bowlers:
    #     all_bowlers = bowler_services.get_all_bowlers()
    # elif args.searchbowler:
    #     bowler_hits = bowler_services.bowler_search(args.searchbowler)
    #     for each_hit in bowler_hits:
    #         print(f"id: {each_hit.id}, name: {each_hit.name}")
    elif args.getsinglebowler:
        bowler_service.get_single_bowler(args.getsinglebowler)
    # elif args.addsingleweek:
    #     add_week()
    # elif args.add_all_weeks:
    #     week_service.add_all_weeks()

