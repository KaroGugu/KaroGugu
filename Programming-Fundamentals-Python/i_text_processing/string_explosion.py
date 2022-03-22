text = input()

strength = 0  # Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
new_text = ""  # print the final string

for index in range(len(text)):
    if text[index] != ">" and strength > 0:  # the moment for explosion
        strength -= 1

    elif text[index] == ">":   # If you find another explosion mark ('>') while deleting characters
        strength += int(text[index + 1])  # you should add the strength to your previous explosion
        new_text += text[index]  # should not delete the explosion character – '>'

    else:
        new_text += text[index]

print(new_text)
