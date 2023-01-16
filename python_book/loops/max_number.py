from sys import maxsize

count = int(input())

max_number = -maxsize
for _ in range(count):
    number = int(input())
    max_number = max(max_number, number)

print(max_number)
