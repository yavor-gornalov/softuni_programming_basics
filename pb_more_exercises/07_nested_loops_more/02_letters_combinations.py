# https://judge.softuni.org/Contests/Practice/Index/1381#1

start_letter = input()
end_letter = input()
exception_letter = input()

ord_ex = ord(exception_letter)
count = 0
for i in range(ord(start_letter), ord(end_letter) + 1):
    for j in range(ord(start_letter), ord(end_letter) + 1):
        for k in range(ord(start_letter), ord(end_letter) + 1):
            if i != ord_ex and j != ord_ex and k != ord_ex:
                count += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")
print(count)
