targets = input().split()


command = input()
while command != "End":

    command = command.split()
    to_do = command[0]
    index = int(command[1])
    value = int(command[2])

    if to_do == "Shoot":
        if 0 <= index < len(targets):     # Shoot the target at the index if it exists
            targets[index] = int(targets[index]) - value  # reducing its value by the given power (integer value)
            if targets[index] <= 0:    # Remove the target if it is shot. A target is shot when its value reaches 0
                targets.pop(index)

    elif to_do == "Add":
        if 0 <= index < len(targets):   # at the received index if it exists
            targets.insert(index, value)  # Insert a target with the received value at the received index
        else:
            print("Invalid placement!")

    elif to_do == "Strike": # Remove the target at the given index and the ones before and after it
        if index + value < len(targets) and index - value >= 0:
            for i in range(index - value, index + value + 1):
                targets[i] = ""
        elif index - value >= len(targets) and index + value < 0:
            for i in range(index - value, index + value + 1):
                targets[i] = ""

        else:     # If any of the indices in the range is invalid, print: "Strike missed!"
            print("Strike missed!")

    command = input()

targets = [str(x) for x in targets if x != ""]
print("|".join(targets))