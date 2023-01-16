n = int(input())

for i in range(1, n + 1):
    print("*", end="")
    for j in range(1, n):
        print(" *", end="")
    print()
