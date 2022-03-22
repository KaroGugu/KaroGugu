numbers = int(input())

left_sum = 0
right_sum = 0

for number in range(0, numbers):
    numbers_left_side = int(input())
    left_sum += numbers_left_side

for number in range(numbers):
    numbers_right_side = int(input())
    right_sum += numbers_right_side

difference = abs(left_sum - right_sum)

if difference == 0:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")