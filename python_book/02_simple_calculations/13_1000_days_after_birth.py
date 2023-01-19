# https://judge.softuni.org/Contests/Practice/Index/1047#12

from datetime import datetime, timedelta

day, month, year = map(int, input().split("-"))

birth_date = datetime(day=day, month=month, year=year)

thousand_date = birth_date + timedelta(days=1000)

thousand_date = thousand_date.strftime("%d-%m-%Y")

print(thousand_date)
