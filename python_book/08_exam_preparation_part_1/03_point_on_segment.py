# https://judge.softuni.org/Contests/Practice/Index/1059#2

start = int(input())
end = int(input())
point = int(input())

text = "out"
left = min(start, end)
right = max(start, end)
if left <= point <= right:
    text = "in"

distance = min(abs(start - point), abs(end - point))

print(f"{text}\n{distance}")
