data = input()

index = 0
current_string = ""
final_result = ""

while index < len(data):
    if not data[index].isdigit():  # convert the letters to uppercase for each string
        current_string += data[index]
        index += 1

    else:  # if index is number   # print letters repeatedly N times
        current_number = ""
        while data[index].isdigit():  # if number is 2-digit
            current_number += data[index]
            index += 1
            if index == len(data):
                break

        current_number = int(current_number)  # The repeat count for each string will be an integer in the range [0-20]
        output = current_string.upper() * current_number
        final_result += output
        current_string = ""

print(f"Unique symbols used: {len(set(final_result))}")
print(final_result)
