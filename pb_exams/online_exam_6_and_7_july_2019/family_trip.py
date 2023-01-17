budget = float(input())
night_count = int(input())
night_price = float(input())
additional_costs_percent = int(input())

if night_count > 7:
    night_price -= 0.05 * night_price

total_cost = night_count * night_price + additional_costs_percent * budget / 100

diff = budget - total_cost

if diff >= 0:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{abs(diff):.2f} leva needed.")
