nums = []

while True:
    num = input()
    if num == "Stop":
        break
    num = int(num)
    nums.append(num)

if max(nums):
    print(max(nums))
