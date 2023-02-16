# https://judge.softuni.org/Contests/Practice/Index/1745#5

from math import ceil

wall_height = int(input())
wall_weight = int(input())
unpainted_percent = int(input()) / 100

hall_area = 4 * wall_height * wall_weight
painting_area = ceil((1 - unpainted_percent) * hall_area)

command = input()
while not command == "Tired!":
    paint_litters = int(command)
    painting_area -= paint_litters
    if painting_area <= 0:
        break
    command = input()

if painting_area < 0:
    print(f"All walls are painted and you have {abs(painting_area)} l paint left!")
elif painting_area == 0:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"{painting_area} quadratic m left.")
