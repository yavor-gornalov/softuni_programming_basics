# https://judge.softuni.org/Contests/Practice/Index/1699#8

actor_name = input()
academy_points = float(input())
jury_members = int(input())

NOMINATION_POINTS = 1250.5
has_nominated = False
actor_total_points = academy_points
for _ in range(jury_members):
    member_name = input()
    member_points = float(input())
    current_points = len(member_name) * member_points / 2
    actor_total_points += current_points
    if actor_total_points >= NOMINATION_POINTS:
        has_nominated = True
        break

if has_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {NOMINATION_POINTS - actor_total_points:.1f} more!")
