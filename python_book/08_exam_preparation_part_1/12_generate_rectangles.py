# https://judge.softuni.org/Contests/Practice/Index/1059#11

# n = int(input())
# m = int(input())
#
# counter = 0
# for x1 in range(-n, n):
#     for y1 in range(-n, n):
#         for x2 in range(x1 + 1, n + 1):
#             for y2 in range(y1 + 1, n + 1):
#                 area = abs(x2 - x1) * abs(y2 - y1)
#                 if area >= m:
#                     print(f"({x1}, {y1}) ({x2}, {y2}) -> {area}")
#                     counter += 1
# if counter == 0:
#     print("No")

n = int(input())
m = int(input())

count = 0

for left in range(-n, n):
    for top in range(-n, n):
        for right in range(left + 1, n + 1):
            for bottom in range(top + 1, n + 1):
                area = abs(right - left) * abs(bottom - top)
                if area >= m:
                    print('(%d, %d) (%d, %d) -> %d' % (left, top, right, bottom, area))
                    count += 1

if count == 0:
    print('No')
