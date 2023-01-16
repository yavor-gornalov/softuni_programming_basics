bad_tasks_count = int(input())

bad_tasks = 0
marks_total = 0
tasks_total = 0
last_task = ''

while bad_tasks < bad_tasks_count:
    current_task = input()
    if current_task == "Enough":
        break

    tasks_total += 1

    current_mark = float(input())
    if current_mark <= 4:
        bad_tasks += 1

    last_task = current_task
    marks_total += current_mark

if bad_tasks < bad_tasks_count:
    print(f"Average score: {marks_total / tasks_total:.2f}")
    print((f"Number of problems: {tasks_total}"))
    print(f"Last problem: {last_task}")
else:
    print(f"You need a break, {bad_tasks} poor grades.")
