# https://judge.softuni.org/Contests/Practice/Index/1061#1

from datetime import timedelta, date as datatype

star_year = int(input())
end_year = int(input())
magic_weight = int(input())

start_date = datatype(year=star_year, month=1, day=1)
end_date = datatype(year=end_year, month=12, day=31)

found = False
current_date = start_date
while current_date <= end_date:
    # date to single digits
    digits = []
    for char in current_date.strftime("%d%m%Y"):
        digits.append(int(char))

    current_weight = 0
    for index, digit in enumerate(digits):
        if index == len(digits) - 1:
            break
        current_weight += digits[index] * sum(digits[(index+1):])
    if current_weight == magic_weight:
        found = True
        print(current_date.strftime("%d-%m-%Y"))

    current_date += timedelta(days=1)

if not found:
    print("No")
