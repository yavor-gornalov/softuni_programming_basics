# https://judge.softuni.org/Contests/Practice/Index/2275#6

days_count = int(input())
total_food = float(input())

dog_total, cat_total, food_total, cookies_total = 0, 0, 0, 0
for i in range(1, days_count + 1):
    dog_food = int(input())
    dog_total += dog_food

    cat_food = int(input())
    cat_total += cat_food

    food_per_day = dog_food + cat_food
    if i % 3 == 0:
        cookies = 0.10 * food_per_day
        cookies_total += cookies

    food_total += food_per_day

food_percent, dog_percent, cat_percent = 0, 0, 0
if total_food > 0:
    food_percent = 100 * food_total / total_food
    dog_percent = 100 * dog_total / food_total
    cat_percent = 100 * cat_total / food_total


print(f"Total eaten biscuits: {round(cookies_total)}gr.")
print(f"{food_percent:.2f}% of the food has been eaten.")
print(f"{dog_percent:.2f}% eaten from the dog.")
print(f"{cat_percent:.2f}% eaten from the cat.")
