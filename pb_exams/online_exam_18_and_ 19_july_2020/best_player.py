top_scorer_name = ''
best_score_result = 0
hat_trick_flag = False
while best_score_result < 10:
    player_name = input()
    if player_name == "END":
        break
    goals_scored = int(input())
    if goals_scored > best_score_result:
        top_scorer_name = player_name
        best_score_result = goals_scored
    if goals_scored >= 3:
        hat_trick_flag = True
    else:
        hat_trick_flag = False

print(f"{top_scorer_name} is the best player!")
if hat_trick_flag:
    print(f"He has scored {best_score_result} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score_result} goals.")
