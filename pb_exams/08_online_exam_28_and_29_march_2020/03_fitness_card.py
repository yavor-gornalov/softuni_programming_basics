# https://judge.softuni.org/Contests/Practice/Index/2275#5

card_budget = float(input())
gender = input()
age = int(input())
sport = input()

card_price = 0
if gender == "m":
    if sport == "Gym":
        card_price = 42
    elif sport == "Boxing":
        card_price = 41
    elif sport == "Yoga":
        card_price = 45
    elif sport == "Zumba":
        card_price = 34
    elif sport == "Dances":
        card_price = 51
    elif sport == "Pilates":
        card_price = 39
elif gender == "f":
    if sport == "Gym":
        card_price = 35
    elif sport == "Boxing":
        card_price = 37
    elif sport == "Yoga":
        card_price = 42
    elif sport == "Zumba":
        card_price = 31
    elif sport == "Dances":
        card_price = 53
    elif sport == "Pilates":
        card_price = 37

if age <= 19:
    card_price -= 0.20 * card_price

balance = card_budget - card_price

if balance < 0:
    print(f"You don't have enough money! You need ${abs(balance):.2f} more.")
else:
    print((f"You purchased a 1 month pass for {sport}."))
