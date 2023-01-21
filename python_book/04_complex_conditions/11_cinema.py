# https://judge.softuni.org/Contests/Practice/Index/1051#10

# user input
screening_type = input().lower()
rows = int(input())
cols = int(input())

# logics
price = 0
if screening_type == "premiere":
    price = 12.00
elif screening_type == "normal":
    price = 7.5
elif screening_type == "discount":
    price = 5.0

total_seats = rows * cols
income = total_seats * price

# console output
print(f"{income:.2f}")
