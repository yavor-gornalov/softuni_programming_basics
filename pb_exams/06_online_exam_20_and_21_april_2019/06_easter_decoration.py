# https://judge.softuni.org/Contests/Practice/Index/1637#11

customers_count = int(input())

total_items_count = 0
total_items_cost = 0

for _ in range(customers_count):
    current_items_count = 0
    current_items_cost = 0
    while True:
        item = input()
        if item == "Finish":
            break
        elif item == "basket":
            current_items_cost += 1.50
        elif item == "wreath":
            current_items_cost += 3.80
        elif item == "chocolate bunny":
            current_items_cost += 7.00
        current_items_count += 1

    if current_items_count % 2 == 0:
        current_items_cost -= 0.20 * current_items_cost
    print(f"You purchased {current_items_count} items for {current_items_cost:.2f} leva.")
    total_items_count += current_items_count
    total_items_cost += current_items_cost

average_items_cost = total_items_cost / customers_count
print(f"Average bill per client is: {average_items_cost:.2f} leva.")
