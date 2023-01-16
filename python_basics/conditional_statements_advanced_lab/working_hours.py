# user input
hour = int(input())
day = input()

# logics
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weekend = ["Sunday"]

text = "closed"
if day in working_days:
    if 10 <= hour <= 18:
        text = "open"

# console output
print(text)
