from math import ceil

first_employee_capacity_per_hour = int(input())
second_employee_capacity_per_hour = int(input())
third_employee_capacity_per_hour = int(input())
total_students_count = int(input())

breaks_counter = 0 # Every fourth hour, all employees have a break, so they don't work for an hour
total_employee_capacity_per_hour = first_employee_capacity_per_hour + second_employee_capacity_per_hour \
                                   + third_employee_capacity_per_hour

all_time_needed = ceil(total_students_count / total_employee_capacity_per_hour)


if all_time_needed > 3:# Every fourth hour, all employees have a break, so they don't work for an hour
    if all_time_needed % 3 !=0:
        breaks_counter = all_time_needed // 3
    else:
        breaks_counter = (all_time_needed // 3) - 1

new_time = all_time_needed + breaks_counter

print(f"Time needed: {new_time}h.")