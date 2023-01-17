trunk_capacity = float(input())

i = 0
free_space = trunk_capacity
suitcase_volume = float(input())
while suitcase_volume != "End":
    i += 1
    suitcase_volume = float(suitcase_volume)
    if i % 3 == 0:
        suitcase_volume += 0.10 * suitcase_volume

    if free_space < suitcase_volume:
        print("No more space!")
        i -= 1
        break

    free_space -= suitcase_volume
    suitcase_volume = input()
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {i} suitcases loaded.")




