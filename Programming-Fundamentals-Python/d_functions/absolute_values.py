def absolute_values():
    numbers = input().split()
    list = []

    for index in range(len(numbers)):
        current_number = float(numbers[index])
        absolute_number = abs(current_number)
        list.append(absolute_number)
    print(list)

absolute_values()