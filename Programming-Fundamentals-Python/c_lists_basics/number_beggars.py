sum_list = input().split(", ")
number_of_beggars = int(input())

final_list = []
counter_of_index = 0
temporary_sum = 0

sum_list_as_digits = []   # sum_list_as_digits = [int(i) for i in sum_list]
for index in range(len(sum_list)):
    sum_list_as_digits.append(int(sum_list[index]))

while counter_of_index < number_of_beggars:
    for element in range(counter_of_index, len(sum_list_as_digits), number_of_beggars):
        temporary_sum += sum_list_as_digits[element]

    final_list.append(temporary_sum)
    temporary_sum = 0
    counter_of_index += 1

print(final_list)

