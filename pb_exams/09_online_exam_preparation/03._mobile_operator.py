# https://judge.softuni.org/Contests/Practice/Index/1654#2

term = input()
tariff = input()
mobile_data = input()
payment_period = int(input())

monthly_tax = 0
if tariff == "Small":
    monthly_tax = 8.58 if term == "two" else 9.98
elif tariff == "Middle":
    monthly_tax = 17.09 if term == "two" else 18.99
elif tariff == "Large":
    monthly_tax = 23.59 if term == "two" else 25.98
elif tariff == "ExtraLarge":
    monthly_tax = 31.79 if term == "two" else 35.99

if mobile_data == "yes":
    if monthly_tax <= 10:
        monthly_tax += 5.50
    elif monthly_tax <= 30:
        monthly_tax += 4.35
    else:
        monthly_tax += 3.85

total_payment = monthly_tax * payment_period
if term == "two":
    total_payment -= (3.75 * total_payment / 100)

print(f"{total_payment:.2f} lv.")
