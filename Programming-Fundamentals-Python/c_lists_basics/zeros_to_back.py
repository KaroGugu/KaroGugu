numbers_as_string = input().split(", ")

my_list = []
list_zeros = []

for number in numbers_as_string:
    number = int(number)
    if not number == 0:
        my_list.append(number)
    else:
        list_zeros.append(number)

final_list = my_list + list_zeros
print(final_list)