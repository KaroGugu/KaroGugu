def rounded_numebrs():
    numbers = input().split()

    list = []

    for number in range(len(numbers)):
        current_number = float(numbers[number])
        rounded = round(current_number)
        list.append(rounded)

    print(list)

rounded_numebrs()