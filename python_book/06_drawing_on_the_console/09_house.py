# https://judge.softuni.org/Contests/Practice/Index/1055#8

n = int(input())

top = 1
if n % 2 == 0:
    top = 2

for i in range((n + 1) // 2):

    for _ in range((n - top) // 2):
        print("-", end="")
    for _ in range(top):
        print("*", end="")
    for _ in range((n - top) // 2):
        print("-", end="")
    print()

    top += 2

for j in range(n // 2):
    print("|", end="")
    for _ in range(n - 2):
        print("*", end="")
    print("|", end="")
    print()
