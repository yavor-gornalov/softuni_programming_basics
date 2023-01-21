# https://judge.softuni.org/Contests/Practice/Index/1059#3

x = int(input())
y = int(input())

is_inside = False
# fig_1
if 2 <= x <= 4 and -3 <= y <= 1:
    is_inside = True
# fig_2
elif 4 <= x <= 10 and -5 <= y <= 3:
    is_inside = True
# fig_3
elif 10 <= x <= 12 and -3 <= y <= 1:
    is_inside = True

if is_inside:
    print("in")
else:
    print("out")
