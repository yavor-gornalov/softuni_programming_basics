# https://judge.softuni.org/Contests/Compete/Index/3880#3

students_count = int(input())

top_marks_count = 0  # [5.00,  6.00]
good_marks_count = 0  # [4.00,  4.99]
poor_marks_count = 0  # [3.00,  3.99]
fail_marks_count = 0  # [2.00,  2.99]
sum_of_marks = 0

for _ in range(students_count):
    current_mark = float(input())
    if 2 <= current_mark < 3:
        fail_marks_count += 1
    elif current_mark < 4:
        poor_marks_count += 1
    elif current_mark < 5:
        good_marks_count += 1
    elif current_mark <= 6:
        top_marks_count += 1

    sum_of_marks += current_mark

print(f"Top students: {100 * top_marks_count / students_count:.2f}%\n"
      f"Between 4.00 and 4.99: {100 * good_marks_count / students_count:.2f}%\n"
      f"Between 3.00 and 3.99: {100 * poor_marks_count / students_count:.2f}%\n"
      f"Fail: {100 * fail_marks_count / students_count:.2f}%\n"
      f"Average: {sum_of_marks / students_count:.2f}")
