number_divisor = int(input())
number_boundary = int(input())

max_multiple = 0

for current_number in range(number_divisor + 1, number_boundary + 1):
    if current_number % number_divisor == 0:
        max_multiple = current_number

print(max_multiple)