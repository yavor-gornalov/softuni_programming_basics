# https://judge.softuni.org/Contests/Practice/Index/1048#0

length = float(input())
width = float(input())

places_per_length = length // 1.2  # working place length = 1.2m
places_per_width = (width - 1) // 0.7  # working place width = 0.7m, corridor width = 1m

working_places_count = int(places_per_width * places_per_length - 3)  # 3 places blocked

print(f"{working_places_count}")
