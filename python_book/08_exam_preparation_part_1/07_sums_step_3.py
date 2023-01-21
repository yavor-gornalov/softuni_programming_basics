# https://judge.softuni.org/Contests/Practice/Index/1059#6

n = int(input())

sum_1 = sum_2 = sum_3 = 0
for i in range(n):
    num = int(input())
    if i % 3 == 0:
        sum_1 += num
    elif i % 3 == 1:
        sum_2 += num
    elif i % 3 == 2:
        sum_3 += num

print(f"sum1 = {sum_1}\nsum2 = {sum_2}\nsum3 = {sum_3}")
