# https://judge.softuni.org/Contests/Practice/Index/1053#6

n = int(input())

left_sum = 0
for _ in range(1, n + 1):
    number = int(input())
    left_sum += number

right_sum = 0
for _ in range(n, 0, -1):
    number = int(input())
    right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")