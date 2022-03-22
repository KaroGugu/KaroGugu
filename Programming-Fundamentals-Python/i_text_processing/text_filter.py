banned_words = input().split(", ")  # a string of banned words, separated by a comma and space
text = input()

for word in banned_words:
    if word in text:
        text = text.replace(word, "*" * len(word))  # number of asterisks "*", equal to the word's length

print(text)