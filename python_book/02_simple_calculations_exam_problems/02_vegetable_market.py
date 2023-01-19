# https://judge.softuni.org/Contests/Practice/Index/1048#1

vegetables_price = float(input())
fruits_price = float(input())
vegetables_quantity = int(input())
fruits_quantity = int(input())

vegetables_cost = vegetables_quantity * vegetables_price
fruits_cost = fruits_quantity * fruits_price

total_profit_euro = (vegetables_cost + fruits_cost) / 1.94

print(total_profit_euro)
