# https://judge.softuni.org/Contests/Compete/Index/3880#4

daily_target = int(input())

MANS_PRICE, LADIES_PRICE, KIDS_PRICE = 15, 20, 10
TOUCH_UP_PRICE, FULL_COLOR_PRICE = 20, 30

daily_profit = 0
target_reached = True
while daily_profit < daily_target:
    command = input()
    if command == "closed":
        target_reached = False
        break
    if command == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            daily_profit += MANS_PRICE
        elif haircut_type == "ladies":
            daily_profit += LADIES_PRICE
        elif haircut_type == "kids":
            daily_profit += KIDS_PRICE
    elif command == "color":
        coloring_type = input()
        if coloring_type == "touch up":
            daily_profit += TOUCH_UP_PRICE
        elif coloring_type == "full color":
            daily_profit += FULL_COLOR_PRICE

if target_reached:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {daily_target - daily_profit}lv. more.")

print(f"Earned money: {daily_profit}lv.")
