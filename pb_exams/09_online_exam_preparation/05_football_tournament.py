# https://judge.softuni.org/Contests/Practice/Index/1745#7

team_name = input()
matches_played = int(input())

if matches_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    points_per_season = 0
    wins, draws, loses = 0, 0, 0
    for _ in range(matches_played):
        current_points = None
        match_result = input()
        if match_result == "W":
            current_points = 3
            wins += 1
        elif match_result == "D":
            current_points = 1
            draws += 1
        elif match_result == "L":
            current_points = 0
            loses += 1
        points_per_season += current_points

    print(f"{team_name} has won {points_per_season} points during this season.\n"
          f"Total stats:\n"
          f"## W: {wins}\n"
          f"## D: {draws}\n"
          f"## L: {loses}\n"
          f"Win rate: {100 * wins / matches_played:.2f}%")
