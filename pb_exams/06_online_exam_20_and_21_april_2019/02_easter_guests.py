# https://judge.softuni.org/Contests/Practice/Index/1637#3

from math import ceil

guests = int(input())
budget = int(input())

easter_bread_count = ceil(guests / 3)
easter_bread_cost = easter_bread_count * 4

eggs_count = guests * 2
eggs_cost = eggs_count * 0.45

total_cost = easter_bread_cost + eggs_cost

balance = budget - total_cost

if balance >= 0:
    print(f"Lyubo bought {easter_bread_count} Easter bread and {eggs_count} eggs.\n"
          f"He has {balance:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.\n"
          f"He needs {abs(balance):.2f} lv. more.")
