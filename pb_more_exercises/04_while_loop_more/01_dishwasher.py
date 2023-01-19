# https://judge.softuni.org/Contests/Practice/Index/1684#0

bottles_count = int(input())
detergent_volume = bottles_count * 750  # ml

dishes_total = 0
pots_total = 0
is_enough = True
is_pot = False
index = 1
while detergent_volume >= 0:
    dishes_count = input()
    if dishes_count == "End":
        break

    dishes_count = int(dishes_count)
    if index < 3:
        index += 1
        detergent_dose = 5
        is_pot = False
    else:
        index = 1
        detergent_dose = 15
        is_pot = True

    detergent_volume -= detergent_dose * dishes_count
    if detergent_volume >= 0:
        is_enough = True
        if is_pot:
            pots_total += dishes_count
        else:
            dishes_total += dishes_count
    else:
        is_enough = False

if is_enough:
    print("Detergent was enough!")
    print(f"{dishes_total} dishes and {pots_total} pots were washed.")
    print(f"Leftover detergent {detergent_volume} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_volume)} ml. more necessary!")
