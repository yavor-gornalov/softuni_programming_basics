# https://judge.softuni.org/Contests/Practice/Index/1851#6

n = int(input())
n += 1

for i in range(n):
    for _ in range(1, n - i):
        print(" ", end="")
    for _ in range(i):
        print("*", end="")
    print(" | ", end="")
    for _ in range(i, 0, -1):
        print("*", end="")
    print()
