# https://judge.softuni.org/Contests/Practice/Index/1699#4

movie_budget = float(input())
destination = input()
season = input()
movie_days = int(input())

shooting_day_cost = None
if destination == "Dubai":
    if season == "Winter":
        shooting_day_cost = 45_000
    elif season == "Summer":
        shooting_day_cost = 40_000

elif destination == "Sofia":
    if season == "Winter":
        shooting_day_cost = 17_000
    elif season == "Summer":
        shooting_day_cost = 12_500

elif destination == "London":
    if season == "Winter":
        shooting_day_cost = 24_000
    elif season == "Summer":
        shooting_day_cost = 20_250

total_price = movie_days * shooting_day_cost

if destination == "Dubai":
    total_price -= 0.30 * total_price
elif destination == "Sofia":
    total_price += 0.25 * total_price

if movie_budget >= total_price:
    print(f"The budget for the movie is enough! We have {movie_budget - total_price:.2f} leva left!")
else:
    print(f"The director needs {total_price - movie_budget:.2f} leva more!")
