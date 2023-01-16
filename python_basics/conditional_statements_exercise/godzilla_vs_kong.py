# user input
budget = float(input())
extras_count = int(input())
clothing_price = float(input())

# logics
decor_price = 0.10 * budget
if extras_count > 150:
    clothing_price -= 0.10 * clothing_price
clothing_total = clothing_price * extras_count
movie_total = decor_price + clothing_total

# console output
if movie_total > budget:
    print("Not enough money!")
    print(f"Wingard needs {movie_total - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - movie_total:.2f} leva left.")
