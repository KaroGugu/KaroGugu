data = input()   # You will be receiving a course name and a student name until you receive the command "end"

courses = {}

while not data == "end":
    course_name, student = data.split(" : ")

    if course_name not in courses:  # If the given course does not exist, add it
        courses[course_name] = []   # courses[course_name] = [student]   else: courses[course_name].append(student)
    courses[course_name].append(student)



    data = input()

# print the courses with their names and total registered users,
# ordered by the number of registeres user in descending order
# for each course print the registered users ordered by name in ascending order (alphabetically)

# sorted_courses = sorted(courses.items(), key=lambda kvpt: -len(kvpt[1]))  # len(kvpt[1]), reversed=True) - if not int
# for course_name,student in sorted_courses:
#     print(f"{course_name}: {len(student)}")
#     for name in sorted(student):
#         print(f"-- {name}")


# print the courses with their names and total registered users. For each course, print the registered users
for course_name,student in courses.items():
    print(f"{course_name}: {len(student)}")

    for name in student:
        print(f"-- {name}")

