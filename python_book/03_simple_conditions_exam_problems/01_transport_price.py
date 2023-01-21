# https://judge.softuni.org/Contests/Practice/Index/1050#0

kilometers_count = int(input())
trip_period = input()

price = 0.0
if kilometers_count < 20:
    if trip_period == "day":
        price = 0.70 + 0.79 * kilometers_count
    elif trip_period == "night":
        price = 0.70 + 0.90 * kilometers_count
elif kilometers_count < 100:
    price = 0.09 * kilometers_count
else:
    price = 0.06 * kilometers_count

print(price)
