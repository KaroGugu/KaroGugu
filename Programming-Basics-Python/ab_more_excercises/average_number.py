numbers = int(input())

index = 0
sum_of_numbers = 0

for num in range(numbers):
    current_number = int(input())
    sum_of_numbers += current_number
    average = sum_of_numbers / numbers

print(f"{average:.2f}")