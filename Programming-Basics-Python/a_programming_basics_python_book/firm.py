from math import floor

hours_for_project = int(input())
available_days = int(input())
number_of_people = int(input())

# work_day = 8 hours
# hours_overtime = 2  # per person

working_days = available_days * 0.90 # През 10% от дните служителите са на обучение и не могат да работят по проекта

overtime_hours_working = number_of_people * (2 * available_days)
hours_working = floor(8 * working_days + overtime_hours_working)

difference = abs(hours_for_project - hours_working)
if hours_for_project <= hours_working:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")