numbers = input()
coded_message = input()

final_message = ""

numbers_list = numbers.split(" ")

# calculating positions
for i in range(len(numbers_list)):
    digits_sum = 0
    for j in str(numbers_list[i]):
        digits_sum += int(j)

    numbers_list[i] = digits_sum

new_coded_message = coded_message

# locating the character in the string
for k in numbers_list:
    if k > len(new_coded_message):
        k = k % len(new_coded_message)
    final_message += new_coded_message[k]

    # creating the final message
    new_coded_message = new_coded_message[0:k] + new_coded_message[k + 1:]

print(final_message)