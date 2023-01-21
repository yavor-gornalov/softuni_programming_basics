# https://judge.softuni.org/Contests/Practice/Index/1051#11

from math import floor

year_type = input().lower()
holidays_per_year = int(input())
home_town_trips = int(input())

weekends_count = 48

playing_days_weekends = 3 * (weekends_count - home_town_trips) / 4
playing_days_weekends += home_town_trips  # hometown always playing

playing_days_holidays = 2 * holidays_per_year / 3
playing_days_total = playing_days_holidays + playing_days_weekends

if year_type == "leap":
    playing_days_total = (1 + 0.15) * playing_days_total
elif year_type == "normal":
    pass

playing_days_total = floor(playing_days_total)

print(playing_days_total)
