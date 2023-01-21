# https://judge.softuni.org/Contests/Practice/Index/1055#3

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('$', end=' ')
    print()
