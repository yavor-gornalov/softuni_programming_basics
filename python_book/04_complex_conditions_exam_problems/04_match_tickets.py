# https://judge.softuni.org/Contests/Practice/Index/1052#3

budget = float(input())
category = input()
count = int(input())

if count < 5:
    budget -= 0.75 * budget
elif count < 10:
    budget -= 0.60 * budget
elif count < 25:
    budget -= 0.50 * budget
elif count < 50:
    budget -= 0.40 * budget
else:
    budget -= 0.25 * budget

sum_for_tickets = 0
if category == "VIP":
    sum_for_tickets = 499.99 * count
elif category == "Normal":
    sum_for_tickets = 249.99 * count

balance = budget - sum_for_tickets
if balance >= 0:
    print(f"Yes! You have {balance:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(balance):.2f} leva.")
