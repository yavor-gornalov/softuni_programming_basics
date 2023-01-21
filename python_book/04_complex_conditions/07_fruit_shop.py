# https://judge.softuni.org/Contests/Practice/Index/1051#6

# user input
fruit = input()
day = input()
quantity = float(input())

# logics
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
fruit_types = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
is_input_valid = day in weekdays and fruit in fruit_types

if is_input_valid:
    day_index = weekdays.index(day)
    fruit_index = fruit_types.index(fruit)
    fruit_prices = [2.50, 1.20, 0.85, 1.45, 2.70, 5.50, 3.85]
    if day_index > 4:
        fruit_prices = [2.70, 1.25, 0.90, 1.60, 3.00, 5.60, 4.20]

    price = fruit_prices[fruit_index]

    total = price * quantity

    print(f"{total:.2f}")
else:
    print("error")
