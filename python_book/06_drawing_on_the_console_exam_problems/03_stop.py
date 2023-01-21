# https://judge.softuni.org/Contests/Practice/Index/1056#2

n = int(input())

start_end = n + 1
middle = 2 * n + 1

# top
print(f"{'.' * start_end}{'_' * middle}{'.' * start_end}")
start_end -= 1
middle -= 2
for _ in range(n):
    print(f"{'.' * start_end}//{'_' * middle}\\\\{'.' * start_end}")
    start_end -= 1
    middle += 2

# middle
print(f"//{'_' * ((middle - 5) // 2)}STOP!{'_' * ((middle - 5) // 2)}\\\\")

# bottom
for i in range(n):
    print(f"{'.' * i}\\\\{'_' * middle}//{'.' * i}")
    middle -= 2
