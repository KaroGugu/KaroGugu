import re

places_on_map = input()


pattern = r"(?<=(/|\=))[A-Z][a-zA-Z][a-zA-Z]+(?=\1)"
# "=" or "/" on both sides (the first and the last symbols must match)  - positive look behind/ahead (?<=) + group
# there should be only letters (the first must be upper-case, other letters could be upper or lower-case)
valid_destinations = [d.group() for d in re.finditer(pattern, places_on_map)]

travel_points = sum([len(d) for d in valid_destinations])  # summing the lengths of all the valid destinations

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")