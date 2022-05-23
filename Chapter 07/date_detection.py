"""
Write a regular expression that can detect dates in the DD/MM/YYYY format.

Currently validates days in month. Need to write validation for leap years
"""

import re

date_ranges = {"01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30, "10": 31,
               "11": 30, "12": 31}


def find_dates(text):
    date_regex = re.compile(r"(\d\d)/(\d\d)/(\d\d\d\d)")
    found_dates = date_regex.search(text)
    day, month, year = found_dates.groups()
    if month in date_ranges:
        max_days = date_ranges[month]
        if int(day) <= max_days:
            print(f"{text} is a valid date.")
        else:
            print(f"Invalid date: Month #{month} has {max_days} days!")
    else:
        print(f"{text} is not a valid date!")


my_text = input("Enter a date: ")
find_dates(my_text)
