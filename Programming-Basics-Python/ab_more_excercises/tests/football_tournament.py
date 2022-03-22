name_of_team = input()
number_of_matches_played = int(input())

points = 0

winner_counter = 0
dawn_counter = 0
lose_counter = 0

total_points = 0
percent_win = 0

for game in range(1, number_of_matches_played + 1):
    result = input()
    if result == "W":
        winner_counter += 1
        points += 3
    elif result == "D":
        dawn_counter += 1
        points += 1
    elif result == "L":
        lose_counter += 1

    total_points = points
    game_played = winner_counter + dawn_counter + lose_counter
    percent_win = winner_counter / game_played * 100


if number_of_matches_played == 0:
    print(f"{name_of_team} hasn't played any games during this season.")

else:
    print(f"{name_of_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {winner_counter}")
    print(f"## D: {dawn_counter}")
    print(f"## L: {lose_counter}")
    print(f"Win rate: {percent_win:.2f}%")