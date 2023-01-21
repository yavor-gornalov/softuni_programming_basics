# https://judge.softuni.org/Contests/Practice/Index/1049#6

first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time

total_minutes = total_time // 60

total_seconds = total_time - 60 * total_minutes

print(f"{total_minutes}:{total_seconds:02d}")
