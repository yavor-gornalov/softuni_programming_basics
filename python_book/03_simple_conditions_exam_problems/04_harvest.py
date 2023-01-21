# https://judge.softuni.org/Contests/Practice/Index/1050#3

from math import ceil, floor

# user input
area = int(input())
grapes_per_m2 = float(input())
wine_demand = int(input())
workers = int(input())

# logics
wine_area = 0.40 * area
wine_produced = wine_area * grapes_per_m2 / 2.5  # 1l wine = 2.5kg grapes

# console output
if wine_produced < wine_demand:
    print(f"It will be a tough winter! More {floor(wine_demand - wine_produced)} liters wine needed.")
else:
    wine_left = ceil(wine_produced - wine_demand)
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{wine_left} liters left -> {ceil(wine_left / workers)} liters per person.")
