string = input()

result = ""
last_letter = ""

for current_letter in string:
    if current_letter != last_letter:
        result += current_letter
        last_letter = current_letter

print(result)