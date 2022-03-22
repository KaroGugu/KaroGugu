from math import ceil

height_of_wall = int(input())
width_of_wall = int(input())
percent_not_painted = int(input())

total_meters = ceil(height_of_wall * width_of_wall * 4)
total_walls_painted = total_meters - total_meters * percent_not_painted / 100

paint_left = 0
command = input()
while command != "Tired!":
    liters_paint = int(command)
    paint_left += liters_paint
    total_walls_painted -= liters_paint
    if total_walls_painted <= 0:
        break

    command = input()

if command == "Tired!":
    print(f"{total_walls_painted:.0f} quadratic m left.")

if paint_left > total_meters - total_meters * percent_not_painted / 100:
    print(f"All walls are painted and you have {abs(total_walls_painted):.0f} l paint left!")
elif paint_left == total_meters - total_meters * percent_not_painted / 100:
    print("All walls are painted! Great job, Pesho!")