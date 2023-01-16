jury_count = int(input())

total_sum_of_marks = 0
total_number_of_presentations = 0
while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    current_sum_of_marks = 0
    for _ in range(jury_count):
        presentation_mark = float(input())
        current_sum_of_marks += presentation_mark

    current_average_mark = current_sum_of_marks / jury_count
    print(f"{presentation_name} - {current_average_mark:.2f}.")

    total_number_of_presentations += 1
    total_sum_of_marks += current_average_mark

total_average_mark = total_sum_of_marks / total_number_of_presentations
print(f"Student's final assessment is {total_average_mark:.2f}.")
