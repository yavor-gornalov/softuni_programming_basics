# https://judge.softuni.org/Contests/Practice/Index/1654#0

strawberries_price = float(input())
bananas_kilos = float(input())
oranges_kilos = float(input())
raspberries_kilos = float(input())
strawberries_kilos = float(input())

raspberries_price = strawberries_price / 2
oranges_price = (1 - 0.40) * raspberries_price
bananas_price = (1 - 0.80) * raspberries_price

strawberries_cost = strawberries_kilos * strawberries_price
bananas_cost = bananas_kilos * bananas_price
oranges_cost = oranges_kilos * oranges_price
raspberries_cost = raspberries_kilos * raspberries_price

total_cost = strawberries_cost + bananas_cost + oranges_cost + raspberries_cost

print(f"{total_cost:.2f}")
