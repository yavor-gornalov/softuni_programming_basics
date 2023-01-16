a = int(input())
b = int(input())
c = int(input())

nums = [a, b, c]
nums.sort()

if nums[0] + nums[1] == nums[2]:
    print(f"{nums[0]} + {nums[1]} = {nums[2]}")
else:
    print("No")
