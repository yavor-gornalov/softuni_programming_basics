# https://judge.softuni.org/Contests/Practice/Index/1658#7

# user input
fuel_type = input()
fuel_litters = float(input())
has_discount = input()

# logics
diesel_price = 2.33
gasoline_price = 2.22
gas_price = 0.93

has_discount = has_discount == "Yes"
if has_discount:
    if fuel_type == "Diesel":
        diesel_price -= 0.12
    elif fuel_type == "Gasoline":
        gasoline_price -= 0.18
    elif fuel_type == "Gas":
        gas_price -= 0.08

total = 0
if fuel_type == "Diesel":
    total = diesel_price * fuel_litters
elif fuel_type == "Gasoline":
    total = gasoline_price * fuel_litters
elif fuel_type == "Gas":
    total = gas_price * fuel_litters

if 20 <= fuel_litters <= 25:
    total -= 0.08 * total
elif fuel_litters > 25:
    total -= 0.1 * total

# console output
print(f"{total:.2f} lv.")
