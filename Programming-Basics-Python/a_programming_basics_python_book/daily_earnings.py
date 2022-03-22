work_days_in_month = int(input())
money_per_day = float(input())
dollar_to_lv = float(input())

salary_for_month = work_days_in_month * money_per_day
bonus = 2.5 * salary_for_month
salary_for_year = salary_for_month * 12 + bonus
tax = salary_for_year * 0.25

money_for_Ivan = (salary_for_year - tax) * dollar_to_lv
money_for_Ivan_per_day = money_for_Ivan / 365
print(f'{money_for_Ivan_per_day:.2f}')