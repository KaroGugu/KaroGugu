numbers = int(input())
previous_number = 0
max_difference = 0

for num in range(numbers):
    first_number = int(input())
    second_number = int(input())

    if num > 0:
        if abs(previous_number - first_number - second_number) > max_difference:
            max_difference = abs(previous_number - first_number - second_number)

    previous_number = first_number + second_number

if max_difference == 0:
    print(f"Yes, value={previous_number}")
else:
    print(f"No, maxdiff={max_difference}")