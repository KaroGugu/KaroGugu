number_of_students = int(input())

grades = {}  # Keep track of all grades for each student
# keep only the students with an average grade higher than or equal to 4.50.

for row in range(number_of_students):
    name_of_student = input()
    grade = float(input())

    if name_of_student not in grades:
        grades[name_of_student] = []
    grades[name_of_student].append(grade)

filtered_grades = {}
for student, grades in grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        filtered_grades[student] = average_grade

# In decending way:
# sorted_best_students = sorted(filtered_grades.items(), key=lambda kvp: -kvp[1])  # ... kvp[1], reverse=True)

for student, grade in filtered_grades.items():   # in sorted_best_students():
    print(f"{student} -> {grade:.2f}")