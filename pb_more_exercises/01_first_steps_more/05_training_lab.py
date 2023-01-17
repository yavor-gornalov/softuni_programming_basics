# https://judge.softuni.org/Contests/Practice/Index/1642#4

room_height = float(input())
room_width = float(input())

places_to_width = int((room_width * 100 - 100) // 70)
places_to_height = int((room_height * 100) // 120)
total_places = places_to_width * places_to_height - 3

print(total_places)
