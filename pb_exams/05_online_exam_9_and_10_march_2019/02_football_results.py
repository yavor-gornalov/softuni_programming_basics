# https://judge.softuni.org/Contests/Practice/Index/1538#2

wins, draws, loses = 0, 0, 0
for _ in range(3):
    game_result = input()
    if game_result[0] > game_result[-1]:
        wins += 1
    elif game_result[0] < game_result[-1]:
        loses += 1
    else:
        draws += 1

print(f"Team won {wins} games.\n"
      f"Team lost {loses} games.\n"
      f"Drawn games: {draws}")
