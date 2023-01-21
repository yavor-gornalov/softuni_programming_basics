# https://judge.softuni.org/Contests/Practice/Index/1059#9

n = int(input())

# top
print('%' * (2 * n))
for i in range((n - 1) // 2):
    print(f"%{' ' * (2 * n - 2)}%")

# middle
print(f"%{' ' * (n - 2)}**{' ' * (n - 2)}%")

# bottom
for i in range((n - 1) // 2):
    print(f"%{' ' * (2 * n - 2)}%")
print('%' * (2 * n))
