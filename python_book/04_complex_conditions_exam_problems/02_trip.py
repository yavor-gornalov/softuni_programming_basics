# https://judge.softuni.org/Contests/Practice/Index/1052#1

budget = float(input())
season = input().lower()

destination = ""
rest_type = ""
cost = 0
if budget <= 100:
    if season == "summer":
        rest_type = "Camp"
        cost = 0.30 * budget
    elif season == "winter":
        rest_type = "Hotel"
        cost = 0.70 * budget
    destination = "Bulgaria"

elif budget <= 1000:
    if season == "summer":
        rest_type = "Camp"
        cost = 0.40 * budget
    elif season == "winter":
        rest_type = "Hotel"
        cost = 0.80 * budget
    destination = "Balkans"
else:
    rest_type = "Hotel"
    cost = 0.90 * budget
    destination = "Europe"

print(f"Somewhere in {destination}\n{rest_type} - {cost:.2f}")
