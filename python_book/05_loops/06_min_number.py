# https://judge.softuni.org/Contests/Practice/Index/1053#5

from sys import maxsize

count = int(input())

min_number = maxsize
for _ in range(count):
    number = int(input())
    min_number = min(min_number, number)

print(min_number)
