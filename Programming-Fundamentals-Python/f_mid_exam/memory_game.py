elements_list = input().split()
command = input()

number_of_moves = 0
win_counter = 0

while command != "end":
    indexes_of_elements = command.split()
    index_first_el = int(indexes_of_elements[0])
    index_second_el = int(indexes_of_elements[1])

    number_of_moves += 1

    remove_first_el = ""
    remove_second_el = ""

    if index_first_el == index_second_el or index_first_el >= len(elements_list) or index_second_el >= len(elements_list) \
            or index_first_el < 0 or index_second_el < 0:
        middle_of_list = len(elements_list) // 2
        elements = elements_list[0:middle_of_list] + [f"-{number_of_moves}a"] + [f"-{number_of_moves}a"] \
                   + elements_list[middle_of_list:]
        print("Invalid input! Adding additional elements to the board")

    else:
        if elements_list[index_first_el] == elements_list[index_second_el]:   # hit two matching elements
            print(f"Congrats! You have found matching elements - {elements_list[index_first_el]}!")
            win_counter += 1
            remove_first_el = elements_list[index_first_el]
            remove_second_el = elements_list[index_second_el]
            elements_list.remove(remove_first_el)
            elements_list.remove(remove_second_el)

        elif elements_list[index_first_el] != elements_list[index_second_el]: # hit two different elements
            print("Try again!")

    if len(elements_list) == 0:   # hit all matching elements before he receives "end"
        print(f"You have won in {win_counter} turns!")
        break

    command = input()

if command == "end":
    print("Sorry you lose :(")
    for i in elements_list:
        print(i, end=" ")