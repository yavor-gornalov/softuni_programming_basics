one_count = int(input())
two_count = int(input())
five_count = int(input())
total = int(input())

for i in range(0, one_count + 1):
    for j in range(0, two_count + 1):
        for k in range(0, five_count + 1):
            if i * 1 + j * 2 + k * 5 == total:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {total} lv.")
