checksum = int(input())

count = 0
a, b, c, d = 0, 0, 0, 0
password = ''
combination = ''
for a in range(1, 10):
    for b in range(1, 10):
        if a >= b:
            continue
        for c in range(1, 10):
            for d in range(1, 10):
                if c <= d:
                    continue
                # checksum = a*b + c*d
                if a * b + c * d == checksum:
                    count += 1
                    combination = f"{a}{b}{c}{d}"
                    print(combination, end=" ")
                    if count == 4:
                        password = combination
    if a == b == c == d == 9:
        print()
if password != '':
    print("Password: " + password)
else:
    print("No!")
