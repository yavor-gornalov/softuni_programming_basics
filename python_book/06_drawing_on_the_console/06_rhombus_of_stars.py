# https://judge.softuni.org/Contests/Practice/Index/1055#5

n = int(input())

for i in range(n):
    for j in range(1, n - i):
        print(" ", end="")
    print("*", end="")
    for k in range(i):
        print(" *", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i, 0, -1):
        print(" ", end="")
    print("*", end="")
    for k in range(i, 1, -1):
        print(" *", end="")
    print()
    