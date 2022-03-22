import re

string = input().lower()
wanted_word = input().lower()

pattern = fr"\b{wanted_word}\b"
matches = re.findall(pattern, string)  # matches = re.findall(pattern, string, flags=re.I)  # case-insensitive


print(len(matches))