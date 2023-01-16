n = int(input())

total = 0
for _ in range(1, n + 1):
    num = int(input())
    total += num

print(f"{total / n:.2f}")
