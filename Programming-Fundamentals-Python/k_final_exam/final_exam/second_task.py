import re

number_of_lines = int(input())

pattern = r"\|(?P<boss>[A-Z]{4,})\|:\#(?P<title>[a-zA-Z]*\s[a-zA-Z]*)\#"

for line in range(number_of_lines):
    text = input()
    valid_inputs = 0

    matches = re.finditer(pattern, text)

    for match in matches:
        boss_and_title = match.groupdict()
        valid_inputs += 1
        print(f'{boss_and_title["boss"]}, The {boss_and_title["title"]}')
        print(f">> Strength: {len(boss_and_title['boss'])}")
        print(f">> Armor: {len(boss_and_title['title'])}")

    if valid_inputs == 0:
        print("Access denied!")