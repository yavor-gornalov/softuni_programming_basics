easter_breads_count = int(input())

leader_name = ""
leader_points = -1
for _ in range(easter_breads_count):
    baker_name = input()
    baker_points = 0
    while True:
        mark = input()
        if mark == "Stop":
            break
        mark = int(mark)
        baker_points += mark

    print(f"{baker_name} has {baker_points} points.")
    if baker_points > leader_points:
        leader_points = baker_points
        leader_name = baker_name
        print(f"{baker_name} is the new number 1!")

print(f"{leader_name} won competition with {leader_points} points!")
