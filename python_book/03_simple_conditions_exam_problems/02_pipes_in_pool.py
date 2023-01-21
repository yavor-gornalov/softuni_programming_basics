# https://judge.softuni.org/Contests/Practice/Index/1050#1

pool_volume = int(input())
first_pipe_flow = int(input())
second_pipe_flow = int(input())
employee_missing_hours = float(input())

first_pipe_volume = first_pipe_flow * employee_missing_hours
second_pipe_volume = second_pipe_flow * employee_missing_hours

pipe_filled_volume = first_pipe_volume + second_pipe_volume

pool_balance = pool_volume - pipe_filled_volume

if pool_balance < 0:
    print(f"For {employee_missing_hours} hours the pool overflows with {abs(pool_balance)} liters.")
else:
    pool_filled_percent = int(100 * (pool_volume - pool_balance) / pool_volume)
    first_pipe_percent = int(100 * first_pipe_volume / pipe_filled_volume)
    second_pipe_percent = int(100 * second_pipe_volume / pipe_filled_volume)
    print(f"The pool is {pool_filled_percent}% full. Pipe 1: {first_pipe_percent}%. Pipe 2: {second_pipe_percent}%.")
