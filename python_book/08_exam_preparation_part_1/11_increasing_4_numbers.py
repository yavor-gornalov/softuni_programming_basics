# https://judge.softuni.org/Contests/Practice/Index/1059#10

a = int(input())
b = int(input())
if b - a < 3:
    print("No")
else:
    for n1 in range(a, b + 1):
        for n2 in range(a, b + 1):
            for n3 in range(a, b + 1):
                for n4 in range(a, b + 1):
                    if n1 < n2 < n3 < n4:
                        print(f"{n1} {n2} {n3} {n4}")
