hundreds_limit = int(input())
tens_limit = int(input())
ones_limit = int(input())

for h in range(1, hundreds_limit + 1):
    if h % 2 != 0:
        continue

    for t in range(1, tens_limit + 1):
        if not 2 <= t <= 7:
            continue
        reminder = 0
        for dev in range(1, t + 1):
            if t % dev == 0:
                reminder += 1
        if reminder != 2:
            continue

        for o in range(1, ones_limit + 1):
            if o % 2 != 0:
                continue
            print(f"{h} {t} {o}")
