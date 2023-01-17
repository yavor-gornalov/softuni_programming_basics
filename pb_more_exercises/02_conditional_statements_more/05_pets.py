# https://judge.softuni.org/Contests/Practice/Index/1658#4

from math import ceil, floor
# user input
days = int(input())
total_food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

# logics
turtle_food_kg = turtle_food_gr / 1000
eaten_food_kg = (dog_food_kg + cat_food_kg + turtle_food_kg) * days

# console output
if eaten_food_kg > total_food_kg:
    print(f"{ceil(eaten_food_kg - total_food_kg)} more kilos of food are needed.")
else:
    print(f"{floor(total_food_kg - eaten_food_kg)} kilos of food left.")
