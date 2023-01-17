# https://judge.softuni.org/Contests/Compete/Index/2419#6

nums = []

while True:
    num = input()
    if num == "Stop":
        break
    num = int(num)
    nums.append(num)

if max(nums):
    print(min(nums))
