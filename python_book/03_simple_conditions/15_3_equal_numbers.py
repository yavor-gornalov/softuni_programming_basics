# https://judge.softuni.org/Contests/Practice/Index/1049#14

first_number = int(input())
second_number = int(input())
third_number = int(input())

equal_flag = False
if first_number == second_number:
    if first_number == third_number:
        equal_flag = True

if equal_flag:
    print("yes")
else:
    print("no")
