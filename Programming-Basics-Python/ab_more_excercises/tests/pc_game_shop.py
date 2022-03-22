number_of_sold_games = int(input())

hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0

for game in range(number_of_sold_games):
    name_of_game = input()

    if name_of_game == "Hearthstone":
        hearthstone_counter += 1
    elif name_of_game == "Fornite":
        fornite_counter += 1
    elif name_of_game == "Overwatch":
        overwatch_counter += 1
    else:
        others_counter += 1

percent_heathstone = hearthstone_counter / number_of_sold_games * 100
percent_fornite = fornite_counter / number_of_sold_games * 100
percent_overwatch = overwatch_counter / number_of_sold_games * 100
percent_others = others_counter / number_of_sold_games * 100

print(f"Hearthstone - {percent_heathstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")