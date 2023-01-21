# https://judge.softuni.org/Contests/Practice/Index/1059#1

bricks_count = int(input())
workers_count = int(input())
car_capacity = int(input())

course_counter = 0

while bricks_count > 0:
    bricks_per_course = workers_count * car_capacity
    bricks_count -= bricks_per_course
    course_counter += 1

print(course_counter)
