# https://judge.softuni.org/Contests/Practice/Index/1381#4

men_count = int(input())
women_count = int(input())
tables_count = int(input())

tables_used = 0
is_finished = False
for m in range(1, men_count + 1):
    for w in range(1, women_count + 1):
        tables_used += 1
        print(f"({m} <-> {w})", end=" ")
        if (m == men_count and w == women_count) or not (tables_count > tables_used):
            is_finished = True
            break
    if is_finished:
        break
