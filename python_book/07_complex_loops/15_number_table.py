# https://judge.softuni.org/Contests/Practice/Index/1057#14

n = int(input())

for row in range(n):
    for col in range(n):
        number = row + col + 1
        if number > n:
            number = 2 * n - number
        print(number, end=" ")
    print()
