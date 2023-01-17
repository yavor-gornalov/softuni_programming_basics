# https://judge.softuni.org/Contests/Compete/Index/2415#7

# user input
day = input()

# logics
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
index = weekdays.index(day)

price = 16
if index == 0 or index == 1 or index == 4:
    price = 12
elif index == 2 or index == 3:
    price = 14

# console output
if index != '':
    print(price)
