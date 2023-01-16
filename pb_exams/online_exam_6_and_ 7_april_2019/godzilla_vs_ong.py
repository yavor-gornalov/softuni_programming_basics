film_budget = float(input())
extras_count = int(input())
extras_suits_price = float(input())

decor_cost = 0.10 * film_budget

if extras_count > 150:
    extras_suits_price -= 0.10 * extras_suits_price

extras_cost = extras_count * extras_suits_price

total_costs = decor_cost + extras_cost

balance = film_budget - total_costs

if balance < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(balance):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {balance:.2f} leva left.")
