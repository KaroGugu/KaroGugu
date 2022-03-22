import re

text = input()

pattern = r"(?P<surrounding>(@|#))(?P<first_word>[A-Za-z]{3,})(?P=surrounding)(?P=surrounding)(?P<second_word>[A-Za-z]{3,})(?P=surrounding)"


matches = re.finditer(pattern, text)
mirror_words = []  # you have to store matches somewhere
count = 0

for match in matches:
    current_words = match.groupdict()
    # If the second word, spelled backward, is the same as the first word and vice versa (casing matters!)
    if current_words["first_word"] == current_words["second_word"][::-1]:
        mirror_words.append(current_words["first_word"])
    count += 1

if count == 0:  # If you don`t find any valid pairs
    print("No word pairs found!")
else:  # If you find valid pairs print their count
    print(f"{count} word pairs found!")

if not mirror_words:  # if the list is empty/ there's no mirror words in the list
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join([f"{word} <=> {word[::-1]}" for word in mirror_words]))

    # for word in mirror_words:
      # print(f"{word} <=> {word[::-1]}")

