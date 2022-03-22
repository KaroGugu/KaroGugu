max_bad_grades = int(input())                # колко най-много лоши оценки може да има

bad_grades = 0
is_expelled = False
total_problems = 0     # counter
average_grade = 0
last_problem = ""

current_problem = input()         # problem_name = input()          # command = input()
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades += 1
        if bad_grades == max_bad_grades:
            is_expelled = True
            break

    average_grade += current_grade
    total_problems += 1
    last_problem = current_problem

    current_problem = input()

if is_expelled:
    print(f"You need a break, {max_bad_grades} poor grades.")       # {bad_grades}
else:
    # if total_problems != 0:
    average_grade /= total_problems      # average_grade = average_grade / total_problems
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_problems}")
    print(f"Last problem: {last_problem}")
