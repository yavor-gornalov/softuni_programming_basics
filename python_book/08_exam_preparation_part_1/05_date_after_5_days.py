# https://judge.softuni.org/Contests/Practice/Index/1059#4

d = int(input())
m = int(input())

days_in_month = 31

if m == 4 or m == 6 or m == 9 or m == 11:
    days_in_month = 30
elif m == 2:
    days_in_month = 28

d += 5
if d > days_in_month:
    d -= days_in_month

    m += 1
    if m > 12:
        m = 1

print(f"{d}.{m:02d}")
