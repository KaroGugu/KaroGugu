from math import floor

hours_needed = int(input())
days_given = int(input())
employees_working_overtime = int(input())

training_no_work = days_given * 0.10
work_day = 8  # hours
hours_overtime = 2 # per person

hours_for_work = (days_given - training_no_work) * 8
work_hours_overtime = employees_working_overtime * (2 * days_given)

total_hours_work = floor(hours_for_work + work_hours_overtime)
difference = abs(hours_needed - total_hours_work)

if total_hours_work >= hours_needed:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")
