# https://judge.softuni.org/Contests/Practice/Index/1050#2

rest_days = int(input())

working_days = 365 - rest_days
year_norm = 30000

playing_time_total = working_days * 63 + rest_days * 127
playing_time = abs(playing_time_total - year_norm)

playing_hours = playing_time // 60
playing_minutes = playing_time % 60

if playing_time_total > year_norm:
    print("Tom will run away")
    print(f"{playing_hours} hours and {playing_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{playing_hours} hours and {playing_minutes} minutes less for play")
