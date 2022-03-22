name_player_one = input()
name_player_two = input()


points_player_one = 0
points_player_two = 0

command = input()
while command != "End of game":
    card_player_one = int(input())
    card_player_two = int(input())

    if card_player_one > card_player_two:
        points_player_one += card_player_one - card_player_two
    elif card_player_two > card_player_one:
        points_player_two += card_player_two - card_player_one
    elif card_player_one == card_player_two:
        card_player_one = int(input())
        card_player_two = int(input())
        print("Number wars!")
        if card_player_one > card_player_two:
            print(f"{name_player_one} is winner with {points_player_one} points")
            break
        else:
            print(f"{name_player_two} is winner with {points_player_two} points")
            break

    points_player_one = points_player_one
    points_player_two = points_player_two

    command = input()

if command == "End of game":
    print(f"{name_player_one} has {points_player_one} points")
    print(f"{name_player_two} has {points_player_two} points")