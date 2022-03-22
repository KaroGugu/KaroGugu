def give_hearts(houses, house_index):
    houses[house_index] -= 2
    # Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2:
    if houses[house_index] <= -2:  # If Cupid jumps to a house where the needed hearts are already 0 = has Val day
        print(f"Place {house_index} already had Valentine's day.")

    elif houses[house_index] <= 0:
        print(f"Place {house_index} has Valentine's day.")

    return houses


houses_in_neighborhood = [int(number) for number in input().split("@")]

cupid_position = 0
command = input().split()

while not command[0] == "Love!":
    length = int(command[1])
    cupid_position += length # Cupid starts at the position of the first house (index 0) and must jump by a given length

    if cupid_position >= len(houses_in_neighborhood):
        # Cupid can have a larger jump length than the size of the neighborhood
        cupid_position = 0  # he should start from the first house again (index 0)

    houses_in_neighborhood = give_hearts(houses_in_neighborhood, cupid_position)

    command = input().split()

print(f"Cupid's last position was {cupid_position}.")

failed_houses = [int(house) for house in houses_in_neighborhood if int(house) > 0]

if failed_houses:  # if failed_houses list exists
    print(f"Cupid has failed {len(failed_houses)} places.")
else:
    print("Mission was successful.")
