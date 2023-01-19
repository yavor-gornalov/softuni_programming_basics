# https://judge.softuni.org/Contests/Practice/Index/1680#4

n = int(input())

intervals = [0, 0, 0, 0, 0, 0]
total = 0
for _ in range(1, n + 1):
    number = int(input())
    if 0 <= number <= 9:
        intervals[0] += 1
        total += 0.20 * number
    elif 10 <= number <= 19:
        intervals[1] += 1
        total += 0.30 * number
    elif 20 <= number <= 29:
        intervals[2] += 1
        total += 0.40 * number
    elif 30 <= number <= 39:
        intervals[3] += 1
        total += 50
    elif 40 <= number <= 50:
        intervals[4] += 1
        total += 100
    else:
        intervals[5] += 1
        total /= 2

print(f"{total:.2f}")
print(f"From 0 to 9: {100 * intervals[0] / n:.2f}%")
print(f"From 10 to 19: {100 * intervals[1] / n:.2f}%")
print(f"From 20 to 29: {100 * intervals[2] / n:.2f}%")
print(f"From 30 to 39: {100 * intervals[3] / n:.2f}%")
print(f"From 40 to 50: {100 * intervals[4] / n:.2f}%")
print(f"Invalid numbers: {100 * intervals[5] / n:.2f}%")
