# https://judge.softuni.org/Contests/Compete/Index/2423#8

area = float(input())

price = area * 7.61
discount = price * 0.18
total_price = price - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")
