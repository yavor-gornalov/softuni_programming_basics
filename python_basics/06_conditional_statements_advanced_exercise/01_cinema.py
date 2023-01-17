# https://judge.softuni.org/Contests/Compete/Index/2416#0

# user input
screening_type = input()
rows = int(input())
cols = int(input())

# logics
price = 0
if screening_type == "Premiere":
    price = 12.00
elif screening_type == "Normal":
    price = 7.5
elif screening_type == "Discount":
    price = 5.0

total_seats = rows * cols
income = total_seats * price

# console output
print(f"{income:.2f}")
