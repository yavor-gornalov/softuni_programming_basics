# https://judge.softuni.org/Contests/Practice/Index/1052#0

exam_hour, exam_minutes = int(input()), int(input())
arrive_hour, arrive_minutes = int(input()), int(input())

exam_time = exam_hour * 60 + exam_minutes
arrive_time = arrive_hour * 60 + arrive_minutes
time_balance = exam_time - arrive_time

message = "Early"
if time_balance < 0:
    message = "Late"
elif 0 <= time_balance <= 30:
    message = "On time"

hour = abs(time_balance) // 60
minutes = abs(time_balance) % 60

print(message)

if message == "Early" and hour > 0:
    print(f"{hour}:{minutes:02d} hours before the start")
elif (message == "Early" or message == "On time") and hour == 0 and minutes > 0:
    print(f"{minutes} minutes before the start")
elif hour == 0 and minutes == 0:
    pass
elif message == "Late" and hour == 0 and  minutes > 0:
    print(f"{abs(minutes)} minutes after the start")
elif message == "Late" and hour > 0:
    print(f"{abs(hour)}:{abs(minutes):02d} hours after the start")
