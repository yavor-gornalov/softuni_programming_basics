# https://judge.softuni.org/Contests/Compete/Index/2415#2

# user input
animal = input()

# logics
text = "unknown"
if animal == "dog":
    text = "mammal"
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    text = "reptile"

# console output
print(text)
