numbers = input().split()

list = []
def sorted_numbers():

    for num in range(len(numbers)):
        current_number = int(numbers[num])
        list.append(current_number)

        sort_numbers = sorted(list)

    print(sort_numbers)

sorted_numbers()