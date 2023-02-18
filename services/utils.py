import datetime
import regex


def get_date():
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

