# https://judge.softuni.org/Contests/Practice/Index/1054#2

inheritance = float(input())
year_to = int(input())

costs = 0
age = 18
for year in range(1800, year_to + 1):
    costs += 12000
    if year % 2 != 0:
        costs += 50 * (age + year - 1800)

balance = inheritance - costs

if balance >= 0:
    print(f"Yes! He will live a carefree life and will have {balance:.2f} dollars left.")
else:
    print(f"He will need {abs(balance):.2f} dollars to survive.")
