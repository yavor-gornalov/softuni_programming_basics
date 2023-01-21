# https://judge.softuni.org/Contests/Practice/Index/1051#1

# user input
product = input()
city = input()
quantity = float(input())

# logics
city_data = ["Sofia", "Plovdiv", "Varna"]
coffee_price = [0.50, 0.40, 0.45]
water_price = [0.80, 0.70, 0.70]
beer_price = [1.20, 1.15, 1.10]
sweets_price = [1.45, 1.30, 1.35]
peanuts_price = [1.60, 1.50, 1.55]

index = city_data.index(city)

total, price = 0, 0
if index != '':
    if product == "coffee":
        price = coffee_price[index]
    elif product == "water":
        price = water_price[index]
    elif product == "beer":
        price = beer_price[index]
    elif product == "sweets":
        price = sweets_price[index]
    elif product == "peanuts":
        price = peanuts_price[index]

total = price * quantity

# console output
print(total)
