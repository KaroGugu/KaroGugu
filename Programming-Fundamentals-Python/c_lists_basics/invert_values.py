list_of_numbers = input().split()   # separate the string into different elements

opposite_numbers = [] # list()

for number in range(len(list_of_numbers)):   # the index of every element of the string
    opposite_number = -int(list_of_numbers[number])
    opposite_numbers.append(opposite_number)
print(opposite_numbers)