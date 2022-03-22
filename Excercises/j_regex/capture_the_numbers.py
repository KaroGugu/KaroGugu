import re

only_numbers = r"\d+"

while True:
    lines_of_strings = input()

    if not lines_of_strings:
        break

    else:
        matches = re.findall(only_numbers, lines_of_strings)
        if matches:
            print(" ".join(matches), end=" ")
