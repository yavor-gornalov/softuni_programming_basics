# https://judge.softuni.org/Contests/Compete/Index/2416#8

days = int(input())
room_type = input()
rating = input()

price = 0
total = 0
discount = 0

if room_type == 'room for one person':
    price = 18.00
elif room_type == 'apartment':
    price = 25.00
elif room_type == 'president apartment':
    price = 35.00

if days < 10:
    if room_type == 'room for one person':
        pass
    elif room_type == 'apartment':
        discount = 30
    elif room_type == 'president apartment':
        discount = 10

elif days <= 15:
    if room_type == 'room for one person':
        pass
    elif room_type == 'apartment':
        discount = 35
    elif room_type == 'president apartment':
        discount = 15

elif days > 15:
    if room_type == 'room for one person':
        pass
    elif room_type == 'apartment':
        discount = 50
    elif room_type == 'president apartment':
        discount = 20

total = (days - 1) * price
total -= discount * total / 100

if rating == 'positive':
    total += 25 * total / 100
elif rating == 'negative':
    total -= 10 * total / 100

print(f"{total:.2f}")
