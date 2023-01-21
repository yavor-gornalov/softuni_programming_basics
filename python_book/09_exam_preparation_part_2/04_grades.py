# https://judge.softuni.org/Contests/Practice/Index/1060#3

students_count = int(input())

poor = medium = good = very_good = excellent = 0
average_grade = 0
for _ in range(students_count):
    grade = float(input())
    average_grade += grade

    if grade < 3:
        poor += 1
    elif grade < 4:
        good += 1
    elif grade < 5:
        very_good += 1
    else:
        excellent += 1

poor_percent = 0
if poor > 0:
    poor_percent = 100 * poor / students_count

medium_percent = 0
if medium > 0:
    medium_percent = 100 * medium / students_count

good_percent = 0
if good > 0:
    good_percent = 100 * good / students_count

very_good_percent = 0
if very_good > 0:
    very_good_percent = 100 * very_good / students_count

excellent_percent = 0
if excellent > 0:
    excellent_percent = 100 * excellent / students_count

average = average_grade / students_count

print(f"Top students: {excellent_percent:.2f}%\n"
      f"Between 4.00 and 4.99: {very_good_percent:.2f}%\n"
      f"Between 3.00 and 3.99: {good_percent:.2f}%\n"
      f"Fail: {poor_percent:.2f}%\n"
      f"Average: {average:.2f}")
