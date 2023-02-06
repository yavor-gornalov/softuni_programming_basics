# https://judge.softuni.org/Contests/Practice/Index/1699#8

actor_name = input()
initial_points = float(input())
jury_count = int(input())

TARGET_POINTS = 1250.5
total_actor_points = initial_points
for _ in range(jury_count):
    if total_actor_points > TARGET_POINTS:
        break
    appraiser_name = input()
    appraiser_points = float(input())
    current_actor_points = len(appraiser_name) * appraiser_points / 2
    total_actor_points += current_actor_points

if total_actor_points > TARGET_POINTS:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_actor_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {TARGET_POINTS - total_actor_points:.1f} more!")
