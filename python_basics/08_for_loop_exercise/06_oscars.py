# https://judge.softuni.org/Contests/Compete/Index/2418#5

actor_name = input()
academy_points = float(input())
evaluators_count = int(input())

actor_points = academy_points

for _ in range(1, evaluators_count + 1):
    evaluator_name = input()
    evaluator_points = float(input())
    if actor_points < 1250.5:
        actor_points += len(evaluator_name) * evaluator_points / 2
    else:
        break

if actor_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - actor_points:.1f} more!")
