flower = input()
count = int(input())
budget = int(input())

total = 0
if flower == "Roses":
    total = 5 * count
    if count > 80:
        total -= 0.1 * total
elif flower == "Dahlias":
    total = 3.8 * count
    if count > 90:
        total -= 0.15 * total
elif flower == "Tulips":
    total = 2.8 * count
    if count > 80:
        total -= 0.15 * total
elif flower == "Narcissus":
    total = 3.0 * count
    if count < 120:
        total += 0.15 * total
elif flower == "Gladiolus":
    total = 2.5 * count
    if count < 80:
        total += 0.2 * total

balance = budget - total
if balance >= 0:
    print(f"Hey, you have a great garden with {count} {flower} and {balance:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(balance):.2f} leva more.")
