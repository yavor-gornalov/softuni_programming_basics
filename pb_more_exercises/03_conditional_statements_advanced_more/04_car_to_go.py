# https://judge.softuni.org/Contests/Practice/Index/1663#3

budget = float(input())
season = input()

percent = 0
car_type = ''
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = 'Cabrio'
        percent = 35
    elif season == "Winter":
        car_type = 'Jeep'
        percent = 65
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = 'Cabrio'
        percent = 45
    elif season == "Winter":
        car_type = 'Jeep'
        percent = 80
else:
    car_class = "Luxury class"
    car_type = 'Jeep'
    percent = 90

car_price = percent * budget / 100

print(f"{car_class}")
print(f"{car_type} - {car_price:.2f}")
