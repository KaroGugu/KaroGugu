numbers = int(input())

left_sum = 0
right_sum = 0

for i in range (0, numbers):
    left_numbers = int(input())
    left_sum += left_numbers

for i in range(0, numbers):
    right_numbers = int(input())
    right_sum += right_numbers

difference = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")