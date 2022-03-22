number_of_students = int(input())

average_grade = 0
excellent_students = 0
good_students = 0
average_students = 0
failed_students = 0

total_result = 0                        # сумата на всички оценки, с помощта на която ще изчислим
                                        # средната оценка на всички студенти

for student in range(number_of_students):
    grade = float(input())
    total_result += grade
    if grade < 3.00:
        failed_students += 1
    elif grade < 4.00:
        average_students += 1
    elif grade < 5.00:
        good_students += 1
    elif grade >= 5.00:
        excellent_students += 1

average_grade = total_result / number_of_students

percent_failed = failed_students * 100 / number_of_students
percent_average = average_students * 100 / number_of_students
percent_good = good_students * 100 / number_of_students
percent_excellent = excellent_students * 100 / number_of_students

print(f"Top students: {percent_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_average:.2f}%")
print(f"Fail: {percent_failed:.2f}%")
print(f"Average: {average_grade:.2f}")