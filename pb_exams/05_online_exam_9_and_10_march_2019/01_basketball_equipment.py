# https://judge.softuni.org/Contests/Practice/Index/1538#1

annual_tax = int(input())

sneakers_price = (1 - 0.40) * annual_tax
equip_price = (1 - 0.20) * sneakers_price
ball_price = equip_price / 4
accessories_price = ball_price / 5

total_cost = annual_tax + sneakers_price + equip_price + ball_price + accessories_price

print(f"{total_cost:.2f}")
