text = input()

encrypted_version = ""

for word in text:
    for letter in word:
        current_letter = chr(ord(letter) + 3)
        encrypted_version += current_letter

print(encrypted_version)