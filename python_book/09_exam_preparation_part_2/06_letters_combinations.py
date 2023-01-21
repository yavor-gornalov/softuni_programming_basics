# https://judge.softuni.org/Contests/Practice/Index/1060#5

start_letter = input()
end_letter = input()
skip_letter = input()

counter = 0
for i in range(ord(start_letter), ord(end_letter) + 1):
    for j in range(ord(start_letter), ord(end_letter) + 1):
        for k in range(ord(start_letter), ord(end_letter) + 1):
            if i != ord(skip_letter) and j != ord(skip_letter) and k != ord(skip_letter):
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")
                counter += 1
print(f"{counter}")
