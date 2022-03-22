name_of_student = input()

grade = 1                                  # клас / година
sum_grades = 0.0
excluded = 0

while grade <= 12:
    year_grade = float(input())             # годишни оценки на ученика
    if year_grade < 4.00:
        excluded += 1
        if excluded > 1:                   # ученикът бъде скъсан повече от един път, то той бива изключен
            break                          # и програмата приключва
        continue
    else:
        grade += 1                       # Ученикът преминава в следващия клас
        sum_grades += year_grade

average_grade = sum_grades / 12          # средната оценка на ученик от цялото му обучение, т.е от 12 години/класа

if excluded > 1:
    print(f"{name_of_student} has been excluded at {grade} grade")

else:
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")