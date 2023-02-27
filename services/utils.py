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
    print("0\tCreate New Team")
    for each_team in all_teams:
        print(f"{each_team.id}\t{each_team.name}")

    valid_team = False
    user_team = 0
    while not valid_team:
        print("\nEnter the team number of tonight's opponent from the list above.")
        print("Choose zero to create a new team.")
        user_team = input("Team number: ")
        user_team = user_team.strip()

        if user_team == "0":
            new_team_created = False
            while not new_team_created:
                new_team_name = input("\nEnter the new team name: ")
                new_team_name = new_team_name.strip()
                team_hit = team_service.search_for_team(new_team_name)
                if team_hit:
                    print("\nThat name already exists in the database.")
                    user_choice = input("Proceed with creating a team with the same name? Yes/no: ")
                    user_choice = user_choice.lower().strip()
                    if user_choice in ["y", "yes"]:
                        print("creating team with the same name")
                        new_team_created = True
                        valid_team = True
                    elif user_choice in ["n", "no"]:
                        print("need to provide a new name")
                    else:
                        print("not a valid option")

                else:
                    print("no team with that name - creating team")
                    new_team_created = True
                    valid_team = True


        elif user_team.isdigit() and user_team in all_teams_list:
            valid_team = True
        else:
            print("That is not a valid team number. PLease try again.")

    print("finally got the hell out of there")
    return user_team


def create_league() -> int:
    pass
