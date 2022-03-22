numbers = list(map(int, input(). split(", ")))

even_list = []

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        even_list.append(index)

print(even_list)