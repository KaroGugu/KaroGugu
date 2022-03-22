numbers = input().split()

def even_numbers ():
    list_of_numbers = []
    list_of_even = []

    for num in numbers:
        current_number = int(num)
        list_of_numbers.append(current_number)

        if current_number % 2 == 0:
            list_of_numbers.remove(current_number)
            list_of_even.append(current_number)

    print(list_of_even)

even_numbers()