# https://judge.softuni.org/Contests/Practice/Index/1062#0

from decimal import Decimal

shopping_money = Decimal(input())

command = ''
while command != "mall.Enter":
    command = input()

purchases = 0
while True:
    command = input()
    if command == "mall.Exit":
        break

    for action in command:
        price = 0
        if action == "*":
            shopping_money += Decimal(10.00)
            continue

        elif action == "%":
            price = Decimal(0.50) * shopping_money
            if shopping_money <= 0:
                continue

        elif action.isalpha():
            if action.isupper():
                price = Decimal(0.50) * ord(action)
            elif action.islower():
                price = Decimal(0.30) * ord(action)

        else:
            price = ord(action)

        if price > shopping_money:
            continue

        shopping_money -= price
        purchases += 1

if purchases == 0:
    print(f"No purchases. Money left: {shopping_money:.2f} lv.")
else:
    print(f"{purchases} purchases. Money left: {shopping_money:.2f} lv.")
