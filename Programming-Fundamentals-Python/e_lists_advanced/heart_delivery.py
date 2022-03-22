def give_hearts(houses, house_index):
    houses[house_index] -= 2
    if houses[house_index] <= -2:
        print(f"Place {house_index} already had Valentine's day.")

    elif houses[house_index] <= 0:
        print(f"Place {house_index} has Valentine's day.")

    return houses


neighbours = [int(number) for number in input().split("@")]

cupid_position = 0
command = input().split()

while not command[0] == "Love!":
    value = int(command[1])
    cupid_position += value

    if cupid_position >= len(neighbours):
        cupid_position = 0

    neighbours = give_hearts(neighbours, cupid_position)

    command = input().split()

print(f"Cupid's last position was {cupid_position}.")

failed_houses = [int(house) for house in neighbours if int(house) > 0]
if failed_houses: # if failed_houses list exists
    print(f"Cupid has failed {len(failed_houses)} places.")
else:
    print("Mission was successful.")
