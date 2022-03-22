capacity = float(input())
bag_counter = 0

while True:
    command = input()            # "End" или до запълване на багажника или Обем на куфар

    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    else:
        command = float(command)

    if (bag_counter + 1) % 3 == 0:             # Обемът на всеки трети куфар трябва да се увеличава с 10%
        command *= 1.1

    if command > capacity:
        print("No more space!")
        break

    bag_counter += 1
    capacity -= command

print(f'Statistic: {bag_counter} suitcases loaded.')