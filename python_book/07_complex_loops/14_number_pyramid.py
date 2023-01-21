# https://judge.softuni.org/Contests/Practice/Index/1057#13

n = int(input())

number = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
        if j >= i:
            print()
        if number > n:
            break
    if number > n:
        break
