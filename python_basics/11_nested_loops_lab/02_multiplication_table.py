# https://judge.softuni.org/Contests/Compete/Index/2421#1

result = 0
for a in range(1, 11):
    for b in range(1, 11):
        result = a * b
        print(f"{a} * {b} = {result}")
