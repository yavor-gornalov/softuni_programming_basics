# https://judge.softuni.org/Contests/Practice/Index/1057#9

from math import sqrt

n = int(input())

is_prime = True
if n > 1:
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print("Prime")
else:
    print("Not prime")
