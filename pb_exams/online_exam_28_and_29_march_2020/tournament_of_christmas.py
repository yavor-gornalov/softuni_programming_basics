tournament_days = int(input())

day_winner = 0
total_money_earned = 0
for _ in range(tournament_days):
    sport = input()
    current_day_money_won = 0
    current_day_wins = 0
    current_day_loses = 0
    while sport != "Finish":
        result = input()
        if result == "win":
            current_day_wins += 1
            current_day_money_won += 20
        elif result == "lose":
            current_day_loses += 1

        sport = input()

    if current_day_wins > current_day_loses:
        day_winner += 1
        current_day_money_won += 0.10 * current_day_money_won

    total_money_earned += current_day_money_won

if day_winner > tournament_days // 2:
    total_money_earned += 0.20 * total_money_earned
    print(f"You won the tournament! Total raised money: {total_money_earned:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_earned:.2f}")
