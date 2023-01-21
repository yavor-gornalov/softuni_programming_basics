# https://judge.softuni.org/Contests/Practice/Index/1052#2

number1 = int(input())
number2 = int(input())
operation = input()

result = ''
if operation == "+" or operation == "-" or operation == "*":
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    else:
        result = number1 * number2

    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"

    print(f"{number1} {operation} {number2} = {result} - {even_odd}")

else:
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        if operation == "/":
            result = number1 / number2
            print(f"{number1} / {number2} = {result:.2f}")
        elif operation == "%":
            result = number1 % number2
            print(f"{number1} % {number2} = {result}")
