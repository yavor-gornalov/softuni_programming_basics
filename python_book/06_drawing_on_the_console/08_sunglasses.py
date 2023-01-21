# https://judge.softuni.org/Contests/Practice/Index/1055#7

n = int(input())

for _ in range(2 * n):
    print("*", end="")
for _ in range(n):
    print(" ", end="")
for _ in range(2 * n):
    print("*", end="")
print()

for row in range(n - 2):
    print("*", end="")
    for _ in range(2 * n - 2):
        print("/", end="")
    print("*", end="")
    if row == int((n - 1) / 2 - 1):
        space = "|"
    else:
        space = " "
    for _ in range(n):
        print(space, end="")
    print("*", end="")
    for _ in range(2 * n - 2):
        print("/", end="")
    print("*\n", end="")

for _ in range(2 * n):
    print("*", end="")
for _ in range(n):
    print(" ", end="")
for _ in range(2 * n):
    print("*", end="")
