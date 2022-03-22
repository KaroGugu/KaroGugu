numbers_list = input().split(" ")

command = input()

while command != "end":
    if command != "decrease":
        action = command.split(" ")
        index1 = int(action[1])
        index2 = int(action[2])

    if command == "decrease":
        for i in range(len(numbers_list)):
            current_i = int(numbers_list[i])
            current_i -= 1
            numbers_list[i] = current_i

    if "swap" in command:
        current = numbers_list[index1]
        numbers_list[index1] = numbers_list[index2]
        numbers_list[index2] = current

    if "multiply" in command:
        multiplication = int(numbers_list[index1]) * int(numbers_list[index2])
        numbers_list[index1] = multiplication

    command = input()

print(*numbers_list, sep=", ")
