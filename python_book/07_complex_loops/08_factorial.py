# https://judge.softuni.org/Contests/Practice/Index/1057#7

n = int(input())

fact = 1
while True:
    fact *= n
    n -= 1
    if not n > 1:
        break

print(fact)
