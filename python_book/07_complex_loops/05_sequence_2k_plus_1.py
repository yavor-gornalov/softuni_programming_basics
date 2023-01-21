# https://judge.softuni.org/Contests/Practice/Index/1057#4

n = int(input())

counter = 1

while counter <= n:
    print(counter)
    counter = 2 * counter + 1

# n = int(input())
#
# sum_numbers = 0
# while True:
#     sum_numbers = 2 * sum_numbers + 1
#     if sum_numbers > n:
#         break
#     print(sum_numbers)
