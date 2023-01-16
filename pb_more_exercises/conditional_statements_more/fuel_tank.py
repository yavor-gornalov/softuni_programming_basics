# user input
fuel_type = input()
fuel_litters = float(input())

# logics
if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
    print("Invalid fuel!")
else:
    if fuel_litters < 25:
        print(f"Fill your tank with {fuel_type.lower() }!")
    else:
        print(f"You have enough {fuel_type.lower()}.")
