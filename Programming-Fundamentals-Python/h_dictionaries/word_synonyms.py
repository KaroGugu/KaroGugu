count_of_words = int(input())

synonyms = {}

for i in range(count_of_words):   # You will be receiving a word and a synonym each on a separate line
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")