import re

dates = input()
expression = r"(?P<Day>\d{2})(?P<separator>[./-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})"

matches = re.finditer(expression, dates)

for match in matches:
    day = match.group("Day")
    month = match.group("Month")
    year = match.group("Year")

    print(f"Day: {day}, Month: {month}, Year: {year}")
