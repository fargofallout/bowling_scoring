import datetime
import regex

from services import team_service


def get_date() -> datetime:
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

    return date_as_datetime


def get_week_num() -> int:
    num_regex = regex.compile(r"\d{1,2}")
    week_number = input("Week number: ")
    valid_input = False
    while not valid_input:
        week_number = week_number.strip()
        week_num_match = num_regex.search(week_number)

        if not week_num_match:
            week_number = "Not a valid week. Try again: "
            valid_input = False
        else:
            week_number = int(week_number)
            valid_input = True

    return week_number


def display_weeks(all_weeks: list) -> int:

    all_week_dict = {x.week_number: x.id for x in all_weeks}

    print("Week Number\tDate")
    for each_week in all_weeks:
        print(f"{each_week.week_number}\t{each_week.date.date()}")

    valid_week = False
    user_week = 0
    while not valid_week:
        user_week = input("\nEnter the number for the current week from the list above: ")

        user_week = user_week.strip()
        if user_week.isdigit() and user_week in all_week_dict:
            valid_week = True
        else:
            print("That is not a valid week number. Please try again.")

    return all_week_dict[user_week]


def display_teams(all_teams: list) -> int:
    all_teams_list = [x.id for x in all_teams]

    # TODO: figure out how to use f strings to make tabular data line up in columns
    print("\n\nTeam Number\tTeam Name")
    for each_team in all_teams:
        print(f"{each_team.id}\t{each_team.name}")

    valid_team = False
    user_team = 0
    while not valid_team:
        print("\nEnter the team number of tonight's opponent from the list above.")
        print("If the theam is not in the list, enter -1.")
        user_team = input("Team number: ")
        user_team = user_team.strip()

        if user_team == "-1":
            print("need to create a new team")
            team_hit = team_service.search_for_team("big ern")
            print(team_hit)
        elif user_team.isdigit() and user_team in all_teams_list:
            valid_team = True
        else:
            print("That is not a valid team number. PLease try again.")

    return user_team
