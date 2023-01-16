from sys import maxsize

n = int(input())

min_value = maxsize
max_value = -maxsize

for _ in range(1, n + 1):
    number = int(input())
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

print(f"Max number: {max_value}")
print(f"Min number: {min_value}")
