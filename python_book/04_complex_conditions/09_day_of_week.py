# https://judge.softuni.org/Contests/Practice/Index/1051#8

# user input
day = int(input())

# logics
week_day = "Error"
if day == 1:
    week_day = "Monday"
elif day == 2:
    week_day = "Tuesday"
elif day == 3:
    week_day = "Wednesday"
elif day == 4:
    week_day = "Thursday"
elif day == 5:
    week_day = "Friday"
elif day == 6:
    week_day = "Saturday"
elif day == 7:
    week_day = "Sunday"

# console output
print(week_day)
