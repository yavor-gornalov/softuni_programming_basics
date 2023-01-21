# https://judge.softuni.org/Contests/Practice/Index/1051#5

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

# {x1, y1} – {x2, y2}

text = "Inside / Outside"
if x1 <= x <= x2 and y == y1:
    text = "Border"

if x1 <= x <= x2 and y == y2:
    text = "Border"

if y1 <= y <= y2 and x == x1:
    text = "Border"

if y1 <= y <= y2 and x == x2:
    text = "Border"

print(text)
