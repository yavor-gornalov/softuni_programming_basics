# https://judge.softuni.org/Contests/Practice/Index/1061#0

# # tribonacci inputs
a = int(input())
b = int(input())
c = int(input())

# spiral inputs
spiral_start = int(input())
spiral_step = int(input())

MAX_NUMBER = 1000000

# tribonacci sequence
last_c = c
tribonacci_numbers = [a, b, c]
while True:
    last_c = a + b + c
    if last_c > MAX_NUMBER:
        break
    tribonacci_numbers.append(last_c)
    a = b
    b = c
    c = last_c

# spiral sequence
spiral_current = spiral_start
spiral_numbers = [spiral_current]
spiral_count = 0
spiral_step_mul = 1
while True:
    spiral_current += spiral_step * spiral_step_mul
    if spiral_current > MAX_NUMBER:
        break
    spiral_numbers.append(spiral_current)
    spiral_count += 1
    if spiral_count % 2 == 0:
        spiral_step_mul += 1

found = False
for i in range(0, len(tribonacci_numbers)):
    for j in range(0, len(spiral_numbers)):
        if tribonacci_numbers[i] == spiral_numbers[j]:
            print(tribonacci_numbers[i])
            found = True
            break
    if found:
        break
if not found:
    print("No")
