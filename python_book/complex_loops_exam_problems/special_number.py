special_number = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if special_number % a == 0 \
                        and special_number % b == 0 \
                        and special_number % c == 0 \
                        and special_number % d == 0:
                    print(f"{a}{b}{c}{d}", end=" ")
