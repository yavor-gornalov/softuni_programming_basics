# https://judge.softuni.org/Contests/Compete/Index/3880#2

ONE_PERSON_PRICE, APARTMENT_PRICE, PRESIDENT_PRICE = 18.00, 25.00, 35.00

days_of_stay = int(input())
room_type = input()
evaluation = input()

room_price = None
if days_of_stay < 10:
    if room_type == "room for one person":
        room_price = ONE_PERSON_PRICE
    elif room_type == "apartment":
        room_price = APARTMENT_PRICE * (1 - 0.30)
    elif room_type == "president apartment":
        room_price = PRESIDENT_PRICE * (1 - 0.10)
elif 10 <= days_of_stay <= 15:
    if room_type == "room for one person":
        room_price = ONE_PERSON_PRICE
    elif room_type == "apartment":
        room_price = APARTMENT_PRICE * (1 - 0.35)
    elif room_type == "president apartment":
        room_price = PRESIDENT_PRICE * (1 - 0.15)
else:
    if room_type == "room for one person":
        room_price = ONE_PERSON_PRICE
    elif room_type == "apartment":
        room_price = APARTMENT_PRICE * (1 - 0.50)
    elif room_type == "president apartment":
        room_price = PRESIDENT_PRICE * (1 - 0.20)

total_price = room_price * (days_of_stay - 1) if days_of_stay > 1 else 0

if evaluation == "positive":
    total_price += 0.25 * total_price
elif evaluation == "negative":
    total_price -= 0.10 * total_price

print(f"{total_price:.2f}")
