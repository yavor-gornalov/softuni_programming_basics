from math import floor

tournaments_count = int(input())
ranking_points = int(input())

tournament_points = ranking_points
wins = 0

for _ in range(1, tournaments_count + 1):
    tournament_position = input()
    if tournament_position == "W":
        tournament_points += 2000
        wins += 1
    elif tournament_position == "F":
        tournament_points += 1200
    elif tournament_position == "SF":
        tournament_points += 720

average_points = (tournament_points - ranking_points) / tournaments_count

print(f"Final points: {tournament_points}")
print(f"Average points: {floor(average_points)}")
print(f"{100 * wins / tournaments_count:.2f}%")
