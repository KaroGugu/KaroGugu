time_for_one_car = input().split(" ")
finish_line = len(time_for_one_car) // 2

left_car_total_time = 0
right_car_total_time = 0

for left_index in range(finish_line):
    current_time_left_car = int(time_for_one_car[left_index])
    if current_time_left_car == 0:
        left_car_total_time -= left_car_total_time * 0.20
    else:
        left_car_total_time += current_time_left_car

for right_index in range(len(time_for_one_car) - 1, finish_line, -1):
    current_time_right_car = int(time_for_one_car[right_index])
    if current_time_right_car == 0:
        right_car_total_time -= right_car_total_time * 0.20
    else:
        right_car_total_time += current_time_right_car

if left_car_total_time > right_car_total_time:
    print(f"The winner is right with total time: {right_car_total_time:.1f}")
else:
    print(f"The winner is left with total time: {left_car_total_time:.1f}")