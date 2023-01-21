# https://judge.softuni.org/Contests/Practice/Index/1053#8

input_text = input()

vowel_sum = 0
for char in input_text:
    if char == "a":
        vowel_sum += 1
    elif char == "e":
        vowel_sum += 2
    elif char == "i":
        vowel_sum += 3
    elif char == "o":
        vowel_sum += 4
    elif char == "u":
        vowel_sum += 5

print(vowel_sum)
