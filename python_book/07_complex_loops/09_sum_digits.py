# https://judge.softuni.org/Contests/Practice/Index/1057#8

n = int(input())

sum_digits = 0
while True:
    sum_digits += (n % 10)
    n = n // 10
    if not n > 0:
        break

print(f"Sum of digits: {sum_digits}")
