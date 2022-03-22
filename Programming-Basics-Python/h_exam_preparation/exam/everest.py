start_point = 5364          # базов лагер, който е на 5 364 метра
days_counter = 1            # започва изкачването си от ден първи о
mount_is_climbed = False

command = input()
while not mount_is_climbed:
    if command == "END":
        break

    meters = int(input())   # Изкачени метри
    if command == "Yes":    # дали Атанас ще нощува преди изкачването на следващите метри
        days_counter += 1   # Дали преди изкачването Атанас нощува: Yes -> започва ден 2-ри / следващ ден
        start_point += meters
    elif command == "No":
        start_point += meters


    if start_point >= 8848:
        mount_is_climbed = True
        break
    if days_counter <= 5 and start_point >= 8848:
        mount_is_climbed = True
        break
    elif days_counter >= 5:        # ако са минали повече от 5 дни в изкачване
        break


    command = input()

if mount_is_climbed:
    print(f"Goal reached for {days_counter} days!")
else:
    print(f"Failed!")
    print(f"{start_point}")