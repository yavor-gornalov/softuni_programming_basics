estimated_steps = 10000
steps = 0
while steps < estimated_steps:
    walk_set = input()
    if walk_set == "Going home":
        walk_set = int(input())
        steps += walk_set
        break

    steps += int(walk_set)

if steps < estimated_steps:
    print(f"{estimated_steps - steps} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{steps - estimated_steps} steps over the goal!")
