# https://judge.softuni.org/Contests/Compete/Index/2419#7

student = input()

grade = 1
mark_total = 0
repeat_grade = 0
while grade <= 12 and repeat_grade < 2:
    mark = float(input())
    if mark >= 4:
        grade += 1
        mark_total += mark
    else:
        repeat_grade += 1

average_mark = mark_total / 12
if repeat_grade < 2:
    print(f"{student} graduated. Average grade: {average_mark:.2f}")
else:
    print(f"{student} has been excluded at {grade} grade")
