# https://judge.softuni.org/Contests/Compete/Index/2418#4

tabs_count = int(input())
salary = int(input())

for i in range(1, tabs_count + 1):
    tab_name = input()
    if tab_name == "Facebook":
        salary -= 150
    elif tab_name == "Instagram":
        salary -= 100
    elif tab_name == "Reddit":
        salary -= 50

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
