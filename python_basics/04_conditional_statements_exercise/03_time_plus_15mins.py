# https://judge.softuni.org/Contests/Compete/Index/2414#2

# user input
hour = int(input())
minutes = int(input())

# logics
minutes += 15

if minutes // 60:
    minutes = minutes % 60
    hour += 1

if hour > 23:
    hour = 0

# console output
print(f"{hour}:{minutes:02d}")
