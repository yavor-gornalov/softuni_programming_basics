# https://judge.softuni.org/Contests/Practice/Index/1053#9

from sys import maxsize

n = int(input())

max_number = -maxsize
sum_numbers = 0
for i in range(1, n + 1):
    number = int(input())
    sum_numbers += number
    if number > max_number:
        max_number = number

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(sum_numbers - 2 * max_number)}")
