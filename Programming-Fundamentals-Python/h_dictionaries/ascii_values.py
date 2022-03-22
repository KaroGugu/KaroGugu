list_of_characters = input().split(", ")

occurrences = {word: ord(word) for word in list_of_characters}

print(occurrences)