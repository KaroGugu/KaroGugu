from math import floor

number_of_tournaments = int(input())   # Брой турнири, в които е участвал
start_points = int(input())            # Начален брой точки в ранглистата

points = 0
win_counter = 0

for tournament in range(number_of_tournaments):   # За всеки турнир се прочита отделен ред: Достигнат етап от турнира
    final = input()
    if final == "W":
        points += 2000
        win_counter += 1
    elif final == "F":
        points += 1200
    elif final == "SF":
        points += 720

total_points = start_points + points

average_points_win = points / number_of_tournaments
percent_win = win_counter / number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points_win)}")
print(f"{percent_win:.2f}%")