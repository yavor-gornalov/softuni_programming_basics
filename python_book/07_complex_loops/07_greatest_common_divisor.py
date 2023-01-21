# https://judge.softuni.org/Contests/Practice/Index/1057#6

a = int(input())
b = int(input())

# divisor = min(a, b)
#
# while divisor > 0:
#     if a % divisor == 0 and b % divisor == 0:
#         print(divisor)
#         break
#     divisor -= 1

while b != 0:
    old_b = b
    b = a % b
    a = old_b
print(f"GCD = {a}")
