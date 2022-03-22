energy = 100
coins = 100

is_closed = False
events = input().split("|")

for type_of_event in events:
    temporary_event = type_of_event.split("-")
    temporary_product = temporary_event[0]
    temporary_energy = int(temporary_event[1])
    temporary_coins = int(temporary_event[1])

    if temporary_product == "rest":
        if energy + temporary_energy > 100:
            print(f"You gained 0 energy.")
        else:
            energy += temporary_energy
            print(f"You gained {temporary_energy} energy.")
        print(f"Current energy: {energy}.")

    elif temporary_product == "order":
        if energy - 30 >= 0:
            print(f"You earned {temporary_coins} coins.")
            coins += temporary_coins
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins - temporary_coins > 0:
            print(f"You bought {temporary_product}.")
            coins -= temporary_coins
        else:
            print(f"Closed! Cannot afford {temporary_product}.")
            is_closed = True
            break

if not is_closed:  # is_closed == False
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")