import re

telephone_numbers = input()

matches = re.findall(r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b", telephone_numbers)   # \+359([ -])2 \d{3} \d{4}\b

# matches = re.finditer (r"\+359([ -])2\1\d{3}\1\d{4}\b", telephone_numbers)
# output = list ()
# for match in matches:
#     output.append(match.group)
# print(", ".join(output))

print(", ".join(matches))