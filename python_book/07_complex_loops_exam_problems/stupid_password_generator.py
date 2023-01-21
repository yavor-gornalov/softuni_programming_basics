num = int(input())
ch = int(input())

for a in range(1, num):
    for b in range(1, num):
        for c in range(ch):
            for d in range(ch):
                for e in range(1, num + 1):
                    if e > a and e > b:
                        print(f"{a}{b}{chr(c + ord('a'))}{chr(d + ord('a'))}{e}", end=" ")
