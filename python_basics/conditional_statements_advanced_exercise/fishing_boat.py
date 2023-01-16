budget = int (input())
season = input()
fisher = int(input())

total = 0
if season == "Spring":
    total = 3000
elif season == "Summer" or season == "Autumn":
    total = 4200
elif season == "Winter":
    total = 2600

if fisher <= 6:
    total -= 0.1 * total
elif 7 <= fisher <= 11:
    total -= 0.15 * total
elif fisher >= 12:
    total -= 0.25 * total

if fisher % 2 == 0 and season != "Autumn":
    total -= 0.05 * total

balance = budget - total

if balance >= 0:
    print(f"Yes! You have {balance:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(balance):.2f} leva.")
