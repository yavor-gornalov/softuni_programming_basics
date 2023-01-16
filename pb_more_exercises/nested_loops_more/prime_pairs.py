first_pair = int(input())
second_pair = int(input())
first_diff = int(input())
second_diff = int(input())

for i in range(first_pair, first_pair + first_diff +1):
    reminder = 0
    for n in range(1, i + 1):
        if i % n == 0:
            reminder += 1
    if reminder > 2:
        continue
    for j in range(second_pair, second_pair + second_diff + 1):
        reminder = 0
        for m in range(1, j + 1):
            if j % m == 0:
                reminder += 1
        if reminder > 2:
            continue
        print(f"{i}{j}")
