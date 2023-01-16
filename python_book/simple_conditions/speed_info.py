speed = float(input())

info = ""
if speed <= 10:
    info = "slow"
elif speed <= 50:
    info = "average"
elif speed <= 150:
    info = "fast"
elif speed <= 1000:
    info = "ultra fast"
else:
    info = "extremely fast"

print(info)
