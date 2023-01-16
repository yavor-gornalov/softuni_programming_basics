limit_1 = int(input())
limit_2 = int(input())
limit_3 = int(input())

for i in range(1, limit_1 + 1):
    for j in range(2, limit_2 + 1):
        for k in range(1, limit_3 + 1):
            if i % 2 == 0 and k % 2 == 0:
                reminder = 0
                for m in range(2, j + 1):
                    if j % m == 0:
                        reminder += 1
                if reminder == 1:
                    print(f"{i} {j} {k}")
