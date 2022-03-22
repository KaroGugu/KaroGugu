searched_word = input()
longer_word = input()

while searched_word in longer_word:   # until there is no match
    longer_word = longer_word.replace(searched_word, "")

print(longer_word)