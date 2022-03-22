import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

all_attendances = []

if number_of_lectures == 0:
    print("Max Bonus: 0.")
    print("The student has attended 0 lectures.")

else:
    for student in range(1, number_of_students + 1):
        attendance_count = int(input())
        all_attendances.append(attendance_count)

    total_bonus = math.ceil((max(all_attendances) / number_of_lectures) * (5 + additional_bonus))

    print(f"Max Bonus: {total_bonus}.")
    print(f"The student has attended {max(all_attendances)} lectures.")