# https://judge.softuni.org/Contests/Practice/Index/1055#4

n = int(input())

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if (row == 1 or row == n) and (col == 1 or col == n):
            print("+", end=" ")
        elif (1 < row < n) and (col == 1 or col == n):
            print("|", end=" ")
        else:
            print("-", end=" ")
    print()
