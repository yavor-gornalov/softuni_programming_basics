# https://judge.softuni.org/Contests/Practice/Index/1059#7

from sys import maxsize

n = int(input())

longest_row = counter = 0
num_prev = -maxsize
for i in range(n):
    num = int(input())
    if num > num_prev:
        counter += 1
    else:
        counter = 1

    if counter > longest_row:
        longest_row = counter

    num_prev = num

print(longest_row)
