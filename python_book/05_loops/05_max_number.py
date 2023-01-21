# https://judge.softuni.org/Contests/Practice/Index/1053#4

from sys import maxsize

count = int(input())

max_number = -maxsize
for _ in range(count):
    number = int(input())
    max_number = max(max_number, number)

print(max_number)
