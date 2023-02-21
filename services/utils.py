import datetime
import regex


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
    print("Week Number\tDate")
    for each_week in all_weeks:
        print(f"{each_week.week_number}\t{each_week.date.date()}")
    # CONTINUE HERE: get user selection for week number
    return 2
