import re

number_of_lines = int(input())

pattern = r"(U\$)(?P<username>[A-Z][a-z]+)\1(P\@\$)(?P<password>[a-z]{5,}\d+)\3"

count = 0
for line in range(number_of_lines):
    registration = input()
    count = 0

    matches = re.finditer(pattern, registration)

    for match in matches:
        count += 1

        current_registration = match.groupdict()

        print("Registration was successful")
        print(f"Username: {match[2]}, Password: {match[4]}")

    if count == 0:
        print("Invalid username or password")

print(f"Successful registrations: {count}")