# https://judge.softuni.org/Contests/Practice/Index/1051#0

# user input
age = float(input())
gender = input()

# logics
text = ""
if gender == "m":
    if age < 16:
        text = "Master"
    else:
        text = "Mr."
elif gender == "f":
    if age < 16:
        text = "Miss"
    else:
        text = "Ms."

# console output
print(text)
