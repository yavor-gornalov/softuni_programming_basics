# https://judge.softuni.org/Contests/Practice/Index/1060#0

initial_speed = int(input()) / 60  # speed in km per minute
first_time = int(input())
second_time = int(input())
finish_time = int(input())

first_distance = initial_speed * first_time

second_speed = (1 + 0.10) * initial_speed
second_distance = second_speed * second_time

finish_speed = (1 - 0.05) * second_speed
finish_distance = finish_speed * finish_time

total_distance = finish_distance + second_distance + first_distance

print(f"{total_distance:.2f}")
