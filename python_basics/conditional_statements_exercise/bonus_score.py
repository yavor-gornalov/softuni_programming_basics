# user input
input_number = int(input())
bonus = 0

# logics
if input_number <= 100:
    bonus += 5
elif input_number <= 1000:
    bonus += input_number * 0.2
else:
    bonus += input_number * 0.1

if input_number % 2 == 0:
    bonus += 1

if input_number % 10 == 5:
    bonus += 2

# console output
print(bonus)
print(input_number + bonus)
