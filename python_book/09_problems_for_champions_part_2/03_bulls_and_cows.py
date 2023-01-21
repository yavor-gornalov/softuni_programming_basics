# https://judge.softuni.org/Contests/Practice/Index/1062#2

guess_number = input()
target_bulls = int(input())
target_cows = int(input())

solution_found = False

for digit_1 in range(1, 10):
    for digit_2 in range(1, 10):
        for digit_3 in range(1, 10):
            for digit_4 in range(1, 10):
                guess_digit_1 = int(guess_number[0:1])
                guess_digit_2 = int(guess_number[1:2])
                guess_digit_3 = int(guess_number[2:3])
                guess_digit_4 = int(guess_number[3:4])

                digit_to_check_1 = digit_1
                digit_to_check_2 = digit_2
                digit_to_check_3 = digit_3
                digit_to_check_4 = digit_4

                current_bulls = 0
                current_cows = 0

                if digit_to_check_1 == guess_digit_1:
                    current_bulls += 1
                    guess_digit_1 = -1
                    digit_to_check_1 = -2
                if digit_to_check_2 == guess_digit_2:
                    current_bulls += 1
                    guess_digit_2 = -1
                    digit_to_check_2 = -2
                if digit_to_check_3 == guess_digit_3:
                    current_bulls += 1
                    guess_digit_3 = -1
                    digit_to_check_3 = -2
                if digit_to_check_4 == guess_digit_4:
                    current_bulls += 1
                    guess_digit_4 = -1
                    digit_to_check_4 = -2

                if digit_to_check_1 == guess_digit_2:
                    current_cows += 1
                    guess_digit_2 = -1
                elif digit_to_check_1 == guess_digit_3:
                    current_cows += 1
                    guess_digit_3 = -1
                elif digit_to_check_1 == guess_digit_4:
                    current_cows += 1
                    guess_digit_4 = -1

                if digit_to_check_2 == guess_digit_1:
                    current_cows += 1
                    guess_digit_1 = -1
                elif digit_to_check_2 == guess_digit_3:
                    current_cows += 1
                    guess_digit_3 = -1
                elif digit_to_check_2 == guess_digit_4:
                    current_cows += 1
                    guess_digit_4 = -1

                if digit_to_check_3 == guess_digit_1:
                    current_cows += 1
                    guess_digit_1 = -1
                elif digit_to_check_3 == guess_digit_2:
                    current_cows += 1
                    guess_digit_2 = -1
                elif digit_to_check_3 == guess_digit_4:
                    current_cows += 1
                    guess_digit_4 = -1

                if digit_to_check_4 == guess_digit_1:
                    current_cows += 1
                    guess_digit_1 = -1
                elif digit_to_check_4 == guess_digit_2:
                    current_cows += 1
                    guess_digit_2 = -1
                elif digit_to_check_4 == guess_digit_3:
                    current_cows += 1
                    guess_digit_3 = -1

                if current_bulls == target_bulls and current_cows == target_cows:
                    if solution_found:
                        print(" ", end="")
                    print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end="")
                    solution_found = True

if not solution_found:
    print("No")
