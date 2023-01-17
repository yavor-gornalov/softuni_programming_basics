# https://judge.softuni.org/Contests/Compete/Index/2419#2

number = int(input())

sum_numbers = 0
while True:
    sum_numbers += int(input())
    if sum_numbers >= number:
        break

print(sum_numbers)
