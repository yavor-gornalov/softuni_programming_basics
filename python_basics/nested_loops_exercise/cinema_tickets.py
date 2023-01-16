total_all = 0
total_student = 0
total_standard = 0
total_kid = 0
while True:
    movie_name = input()
    if movie_name == 'Finish':
        break
    free_places = int(input())

    current_all = 0
    current_student = 0
    current_standard = 0
    current_kid = 0
    while free_places > current_all:
        ticket_type = input()
        if ticket_type == 'End':
            break

        if ticket_type == "student":
            current_student += 1
        elif ticket_type == "standard":
            current_standard += 1
        elif ticket_type == "kid":
            current_kid += 1

        current_all += 1

    occupancy = 100 * current_all / free_places
    print(f"{movie_name} - {occupancy:.2f}% full.")

    total_all += current_all
    total_student += current_student
    total_standard += current_standard
    total_kid += current_kid

student_occupancy = 100 * total_student / total_all
standard_occupancy = 100 * total_standard / total_all
kid_occupancy = 100 * total_kid / total_all

print(f"Total tickets: {total_all}")
print(f"{student_occupancy:.2f}% student tickets.")
print(f"{standard_occupancy:.2f}% standard tickets.")
print(f"{kid_occupancy:.2f}% kids tickets.")
