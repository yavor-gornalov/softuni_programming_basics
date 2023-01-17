# https://judge.softuni.org/Contests/Compete/Index/2424#3

sheets_count = int(input())
sheets_per_hour = int(input())
days = int(input())

hours_per_book = sheets_count // sheets_per_hour
days_per_book = hours_per_book // days

print(days_per_book)
