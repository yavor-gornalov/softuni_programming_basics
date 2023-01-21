# https://judge.softuni.org/Contests/Practice/Index/1049#13

from datetime import datetime, timedelta

hours = int(input())
minutes = int(input())

input_time = datetime(2005, 7, 14, hour=hours, minute=minutes)

new_time = input_time + timedelta(minutes=15)

new_time = new_time.strftime("%H:%M")

if new_time[0] == "0":
    new_time = new_time[1:]

print(new_time)
