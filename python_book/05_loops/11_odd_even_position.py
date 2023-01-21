# https://judge.softuni.org/Contests/Practice/Index/1053#10

from sys import maxsize

n = int(input())

odd_sum, even_sum = 0, 0
odd_min, even_min = maxsize, maxsize
odd_max, even_max = -maxsize, -maxsize

for i in range(1, n + 1):
    number = input()
    if "." in number:
        number = float(number)
    else:
        number = int(number)

    if i % 2 != 0:
        odd_sum += number
        odd_max = max(odd_max, number)
        odd_min = min(odd_min, number)
    else:
        even_sum += number
        even_max = max(even_max, number)
        even_min = min(even_min, number)

odd_extreme = odd_min < maxsize or odd_max > -maxsize
even_extreme = even_min < maxsize or even_max > -maxsize

if odd_sum % 1 == 0:
    odd_sum = int(odd_sum)
if even_sum % 1 == 0:
    even_sum = int(even_sum)

print(f"OddSum={odd_sum},")
if odd_extreme:
    print(f"OddMin={odd_min},\nOddMax={odd_max},")
else:
    print(f"OddMin=No,\nOddMax=No,")

print(f"EvenSum={even_sum},")
if even_extreme:
    print(f"EvenMin={even_min},\nEvenMax={even_max}")
else:
    print(f"EvenMin=No,\nEvenMax=No")
