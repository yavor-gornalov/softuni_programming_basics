# https://judge.softuni.org/Contests/Practice/Index/1051#2

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

# {x1, y1} – {x2, y2}

text = "Inside / Outside"
if x1 <= x <= x2 and y1 <= y <= y2:
    text = "Inside"
else:
    text = "Outside"

print(text)
