students_dictionary = {}

command = input()

while ":" in command:
    info = command.split(":")   # You will be receiving names of students, their ID, and a course
    name, id, course = info[0], info[1], info[2]

    if course not in students_dictionary:
        students_dictionary[course] = {}
    students_dictionary[course][id] = name

    command = input()

course = " ".join(command.split("_"))

for key, value in students_dictionary.items():
    if key == course:  # You should print only the information of the students who have taken the corresponding course
        for id, name in value.items():
            print(f"{name} - {id}")