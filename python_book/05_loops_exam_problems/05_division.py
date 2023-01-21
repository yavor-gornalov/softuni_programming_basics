# https://judge.softuni.org/Contests/Practice/Index/1054#4

numbers_count = int(input())

multiple_of_2, multiple_of_3, multiple_of_4 = 0, 0, 0
for _ in range(numbers_count):
    number = int(input())
    if number % 2 == 0:
        multiple_of_2 += 1
        if number % 4 == 0:
            multiple_of_4 += 1
    if number % 3 == 0:
        multiple_of_3 += 1

multiple_of_2_percent, multiple_of_3_percent, multiple_of_4_percent = 0, 0, 0
if multiple_of_2 > 0:
    multiple_of_2_percent = 100 * multiple_of_2 / numbers_count
if multiple_of_3 > 0:
    multiple_of_3_percent = 100 * multiple_of_3 / numbers_count
if multiple_of_4 > 0:
    multiple_of_4_percent = 100 * multiple_of_4 / numbers_count

print(f"{multiple_of_2_percent:.2f}%\n"
      f"{multiple_of_3_percent:.2f}%\n"
      f"{multiple_of_4_percent:.2f}%")
