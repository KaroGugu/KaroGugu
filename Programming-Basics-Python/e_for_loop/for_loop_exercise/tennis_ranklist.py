from math import floor

number_of_tournaments = int(input())
start_points = int(input())

current_points = 0
tournaments_won = 0

for tournaments in range(number_of_tournaments):
    result = input()
    if result == "W":
        current_points += 2000
        tournaments_won += 1
    elif result == "F":
        current_points += 1200
    elif result == "SF":
        current_points += 720

final_points = current_points + start_points
average_points = current_points / number_of_tournaments
percent_win = (tournaments_won / number_of_tournaments) * 100

print(f'Final points: {final_points}')
print(f"Average points: {floor(average_points)}")
print(f'{percent_win:.2f}%')