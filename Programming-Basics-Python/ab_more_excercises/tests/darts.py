name_of_player = input()

start_points = 301
success_counter = 0
unsuccess_counter = 0

command = input()
while command != "Retire" and start_points != 0:
    pole = command
    points = int(input())

    if pole == "Single":
        points *= 1
        if points > start_points:
            unsuccess_counter += 1
        elif points <= start_points:
            start_points -= points
            success_counter += 1


    elif pole == "Double":
        points *= 2
        if points > start_points:
            unsuccess_counter += 1
        elif points <= start_points:
            start_points -= points
            success_counter += 1


    elif pole == "Triple":
        points *= 3
        if points > start_points:
            unsuccess_counter += 1
        elif points <= start_points:
            start_points -= points
            success_counter += 1

    if start_points == 0:
        print(f"{name_of_player} won the leg with {success_counter} shots.")
        break


if command == "Retire":
    print(f"{name_of_player} retired after {unsuccess_counter} unsuccessful shots.")
