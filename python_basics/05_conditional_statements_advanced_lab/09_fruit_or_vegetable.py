# https://judge.softuni.org/Contests/Compete/Index/2415#8

# user input
product = input()

# logics
fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]

text = "unknown"
if product in fruits:
    text = "fruit"
elif product in vegetables:
    text = "vegetable"

# console output
print(text)
