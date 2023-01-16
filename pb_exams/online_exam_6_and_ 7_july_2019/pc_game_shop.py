game_count = int(input())

hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0
total_games_sold = 0

for game in range(game_count):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone_count += 1
    elif game_name == "Fornite":
        fornite_count += 1
    elif game_name == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1

    total_games_sold += 1

hearthstone_percent = 100 * hearthstone_count / total_games_sold
fornite_percent = 100 * fornite_count / total_games_sold
overwatch_percent = 100 * overwatch_count / total_games_sold
others_percent = 100 * others_count / total_games_sold

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")