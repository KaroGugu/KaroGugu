import re

strings = input()

pattern = r"((?<=\s)([a-z0-9]+[-\.\_a-z0-9]*)@([a-z0-9]+)(-[a-z0-9]+)*\.([a-z\.]+))\b"  # @[a-z\-]+[\.[a-z]+]+
matches = re.findall(pattern, strings)

for match in matches:
    print(match[0])