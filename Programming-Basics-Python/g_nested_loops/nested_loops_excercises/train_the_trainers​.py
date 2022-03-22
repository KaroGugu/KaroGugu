number_of_jury = int(input())
command = input()              # името на презентацията ; команда "Finish"

average_all_grades = 0
presentations_count = 0

while command != 'Finish':

    presentations_count += 1
    current_grades_sum = 0

    for person in range(number_of_jury):
        current_grade = float(input())     # За всяка една презентация на нов ред се четат n - на брой оценки
        current_grades_sum += current_grade

    current_average = current_grades_sum / number_of_jury   # средната оценка от представянето за конкретна презентация

    print(f'{command} - {current_average:.2f}.')

    average_all_grades += current_average

    command = input()

average_assessment = average_all_grades / presentations_count  # средния успех от всички презентации

print(f"Student's final assessment is {average_assessment:.2f}.")