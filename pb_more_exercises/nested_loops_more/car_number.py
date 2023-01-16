start_number = int(input())
end_number = int(input())

for i in range(start_number, end_number + 1):
    for j in range(start_number, end_number + 1):
        for k in range(start_number, end_number + 1):
            for m in range(start_number, end_number + 1):
                check_first_last_digit = i % 2 == 0 and m % 2 != 0 or i % 2 != 0 and m % 2 == 0
                check_middle_digits = (j + k) % 2 == 0
                if check_first_last_digit and check_middle_digits and i > m:
                    print(f"{i}{j}{k}{m}", end=" ")
