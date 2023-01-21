# https://judge.softuni.org/Contests/Practice/Index/1049#15

number = int(input())

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
decades = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

text = ""
if number < 1:
    text = "zero"
elif number < 10:
    text = ones[number]
elif number < 20:
    text = teens[number % 10]
elif number < 100:
    if number % 10 == 0:
        text = f"{decades[number // 10]}"
    else:
        text = f"{decades[number // 10]} {ones[number % 10]}"
else:
    text = "one hundred"

print(text)
