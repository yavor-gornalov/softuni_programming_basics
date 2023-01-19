# https://judge.softuni.org/Contests/Practice/Index/1637#9

from math import ceil

easter_bread_count = int(input())

total_sugar_used, total_flour_used = 0, 0
max_sugar_used, max_flour_used = 0, 0
for _ in range(easter_bread_count):
    current_sugar_used = int(input())
    current_flour_used = int(input())

    if current_sugar_used > max_sugar_used:
        max_sugar_used = current_sugar_used
    if current_flour_used > max_flour_used:
        max_flour_used = current_flour_used

    total_sugar_used += current_sugar_used
    total_flour_used += current_flour_used

sugar_packs = ceil(total_sugar_used / 950)
flour_packs = ceil(total_flour_used / 750)

print(f"Sugar: {sugar_packs}\n"
      f"Flour: {flour_packs}\n"
      f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")
