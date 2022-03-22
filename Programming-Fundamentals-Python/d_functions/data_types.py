def data_type(word, action):
    if word == "int":
        return int(action) * 2
    elif word == "real":
        result = float(action) * 1.5
        return f"{result:.2f}"
    elif word == "string":
        return f"${action}$"


line_input = input()
number_or_word = input()

print(data_type(line_input, number_or_word))
