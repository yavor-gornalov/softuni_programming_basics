# https://judge.softuni.org/Contests/Practice/Index/1053#11

n = int(input())

pair = []
diff = 0
max_diff = 0

for i in range(n):
    num1 = int(input())
    num2 = int(input())
    pair.append(num1 + num2)

    if i > 0:
        diff = abs(pair[i] - pair[i - 1])
        if diff > max_diff:
            max_diff = diff

if max_diff == 0:
    print(f"Yes, value={pair[0]}")
else:
    print(f"No, maxdiff={max_diff}")

