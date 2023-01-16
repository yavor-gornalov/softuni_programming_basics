spare_width = int(input())
spare_length = int(input())
spare_height = int(input())

spare_volume = spare_width * spare_length * spare_height

while spare_volume >= 0:
    boxes_count = input()
    if boxes_count == "Done":
        break
    boxes_count = int(boxes_count)

    spare_volume -= boxes_count

if spare_volume < 0:
    print(f"No more free space! You need {abs(spare_volume)} Cubic meters more.")
else:
    print(f"{spare_volume} Cubic meters left.")
