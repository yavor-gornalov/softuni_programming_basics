bought_food_kilos = int(input())
bought_food_grams = bought_food_kilos * 1000

food_eaten = input()
while food_eaten != "Adopted":
    food_eaten = int(food_eaten)
    bought_food_grams -= food_eaten

    # if bought_food_grams < 0:
    #     break

    food_eaten = input()

if bought_food_grams < 0:
    print(f"Food is not enough. You need {abs(bought_food_grams)} grams more.")
else:
    print(f"Food is enough! Leftovers: {bought_food_grams} grams.")
