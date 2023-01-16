# user input
week_day = input()

# logics
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
text_to_print = "Error"
if week_day in working_days:
    text_to_print = "Working day"
elif week_day in weekend:
    text_to_print = "Weekend"

# console output
print(text_to_print)
