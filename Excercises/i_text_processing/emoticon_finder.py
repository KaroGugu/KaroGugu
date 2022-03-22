text = input()

for letter in range(len(text)):
    if text[letter] == ':':
        print(f":{text[letter + 1]}")
