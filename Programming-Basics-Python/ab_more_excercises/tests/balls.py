from math import floor
balls = int(input())

# colors  red, organge, yellow, white, black

points = 0
counter_red = 0
counter_orange = 0
counter_yellow = 0
counter_white = 0
devides_black = 0
other_colors = 0

total_points = 0

for ball in range(balls):
    color = input()

    if color == "red":
        points += 5
        counter_red += 1
    elif color == "orange":
        points += 10
        counter_orange += 1
    elif color == "yellow":
        points += 15
        counter_yellow += 1
    elif color == "white":
        points += 20
        counter_white += 1
    elif color == "black":
        points /= 2
        devides_black += 1
    else:
        other_colors += 1

total_points += points

print(f"Total points: {floor(total_points)}")
print(f"Points from red balls: {counter_red}")
print(f"Points from orange balls: {counter_orange}")
print(f"Points from yellow balls: {counter_yellow}")
print(f"Points from white balls: {counter_white}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {devides_black}")