# https://judge.softuni.org/Contests/Practice/Index/1680#3

students_count = int(input())

poor_count = middle_count = good_count = very_good_count = 0
grades_total = 0
for _ in range(1, students_count + 1):
    grade = float(input())
    grades_total += grade
    if grade < 3:
        poor_count += 1
    elif grade < 4:
        middle_count += 1
    elif grade < 5:
        good_count += 1
    else:
        very_good_count += 1

print(f"Top students: {100 * very_good_count / students_count:.2f}%")
print(f"Between 4.00 and 4.99: {100 * good_count / students_count:.2f}%")
print(f"Between 3.00 and 3.99: {100 * middle_count / students_count:.2f}%")
print(f"Fail: {100 * poor_count / students_count:.2f}%")
print(f"Average: {grades_total / students_count:.2f}")
