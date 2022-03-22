notes = [0] * 10

command = input()

while not command == "End":
    importance, text = command.split("-")
    current_index = int(importance) - 1
    notes[current_index] = text

    command = input()

print([element for element in notes if not element == 0])