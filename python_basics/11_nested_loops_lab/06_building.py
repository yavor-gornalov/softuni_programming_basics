# https://judge.softuni.org/Contests/Compete/Index/2421#5

floors_count = int(input())
rooms_count = int(input())

for floor in range(floors_count, 0, -1):
    abbreviation = ''
    if floor % 2 == 0:
        abbreviation = 'O'
    else:
        abbreviation = 'A'

    if floor == floors_count:
        abbreviation = 'L'

    for room in range(rooms_count):
        print(f"{abbreviation}{floor}{room}", end=' ')

    print()
