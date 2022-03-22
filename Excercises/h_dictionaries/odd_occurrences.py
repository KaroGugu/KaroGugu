words = input().split()

dictionary = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:   # check for each word (lower case) if it is in the dictionary
        dictionary[word_lower] = 0    # and if it is not, add it
    dictionary[word_lower] += 1

for (key, value) in dictionary.items():  # check if the number of occurrences of the current word is odd
    if value % 2 != 0:
        print(key, end=" ")