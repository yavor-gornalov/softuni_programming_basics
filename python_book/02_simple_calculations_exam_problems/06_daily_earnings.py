# https://judge.softuni.org/Contests/Practice/Index/1048#4

working_days_per_month = int(input())
daily_salary = float(input())
usd_to_bgn = float(input())

yearly_salary = (12 + 2.5) * (daily_salary * working_days_per_month)  # 2.5 month salaries bonus
yearly_salary -= yearly_salary / 4  # 25% taxes

salary_bgn = yearly_salary * usd_to_bgn
daily_average_bgn = salary_bgn / 365

print(f"{daily_average_bgn:.2f}")
