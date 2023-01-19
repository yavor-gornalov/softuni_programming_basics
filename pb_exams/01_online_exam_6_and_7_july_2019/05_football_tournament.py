# https://judge.softuni.org/Contests/Practice/Index/1745#7

football_team = input()
games_played = int(input())

points = 0
wins = 0
draws = 0
loses = 0

for _ in range(games_played):
    game = input()
    if game == "W":
        wins += 1
        points += 3
    elif game == "D":
        draws += 1
        points += 1
    elif game == "L":
        loses += 1
        points += 0

if games_played == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    win_rate = 100 * wins / games_played
    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {win_rate:.2f}%")
