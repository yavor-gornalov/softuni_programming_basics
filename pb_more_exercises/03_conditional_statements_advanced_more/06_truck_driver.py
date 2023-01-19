# https://judge.softuni.org/Contests/Practice/Index/1663#5

season = input()
km_per_month = float(input())

km_price = 0
if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        km_price = 0.75
    elif season == "Summer":
        km_price = 0.90
    elif season == "Winter":
        km_price = 1.05
elif km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        km_price = 0.95
    elif season == "Summer":
        km_price = 1.10
    elif season == "Winter":
        km_price = 1.25
else:
    km_price = 1.45

salary = 4 * (km_price * km_per_month)
salary -= 0.10 * salary

print(f"{salary:.2f}")
