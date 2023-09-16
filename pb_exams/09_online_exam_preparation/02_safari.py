# https://judge.softuni.org/Contests/Practice/Index/1654#1

budget = float(input())
fuel_demanded = float(input())
day_of_week = input()

FUEL_PRICE = 2.10
GUIDE_PRICE = 100

discount = 0
if day_of_week == "Saturday":
    discount = 0.10
elif day_of_week == "Sunday":
    discount = 0.20

total_cost = fuel_demanded * FUEL_PRICE + GUIDE_PRICE
final_cost = (1 - discount) * total_cost

if final_cost > budget:
    print(f"Not enough money! Money needed: {final_cost - budget:.2f} lv.")
else:
    print(f"Safari time! Money left: {budget - final_cost:.2f} lv.")
