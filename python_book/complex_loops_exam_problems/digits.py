number = int(input())

a = number // 100
b = (number % 100) // 10
c = number % 10

n = a + b
m = a + c
for _ in range(n):
    for _ in range(m):
        if number % 5 == 0:
            number -= a
        elif number % 3 == 0:
            number -= b
        else:
            number += c
        print(number, end=" ")
    print()
