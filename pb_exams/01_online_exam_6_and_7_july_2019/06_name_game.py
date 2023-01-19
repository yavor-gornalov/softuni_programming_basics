# https://judge.softuni.org/Contests/Practice/Index/1745#8

best_score = 0
best_player_name = ""
while True:
    player_name = input()
    if player_name == "Stop":
        break

    player_result = 0
    for ch in player_name:
        num = int(input())
        if num == ord(ch):
            player_result += 10
        else:
            player_result += 2

    if player_result >= best_score:
        best_score = player_result
        best_player_name = player_name

print(f"The winner is {best_player_name} with {best_score} points!")
