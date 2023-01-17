# https://judge.softuni.org/Contests/Compete/Index/2424#6

chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

chicken_price = chicken_menus * 10.35
fish_price = fish_menus * 12.40
vegan_price = vegan_menus * 8.15

total_meal = chicken_price + fish_price + vegan_price
sweets = total_meal * 0.20

total_meal += sweets

final_sum = total_meal + 2.50  # delivery

print(final_sum)
