from math import ceil

# user input
movie_name = input()
movie_time = int(input())
break_time = int(input())

# logics
lunch_time = break_time / 8
rest_time = break_time / 4

watching_time = break_time - (lunch_time + rest_time)

if movie_time > watching_time:
    print(f"You don't have enough time to watch {movie_name},"
          f" you need {ceil(movie_time - watching_time)} more minutes.")
else:
    print(f"You have enough time to watch {movie_name} and "
          f"left with {ceil(watching_time - movie_time)} minutes free time.")
