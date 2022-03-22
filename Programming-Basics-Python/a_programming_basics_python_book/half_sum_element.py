import sys

numbers = int(input())

sum_numbers = 0
max_number = -sys.maxsize

for number in range(numbers):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    sum_other_numbers = sum_numbers - max_number
    difference = abs(max_number - (sum_numbers - max_number))
    print("No")
    print(f'Diff = {difference}')
