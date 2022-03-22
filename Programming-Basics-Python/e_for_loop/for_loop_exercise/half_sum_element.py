import sys

numbers = int(input())         # n-на брой цели числа, които ще въртим в цикъла

sum_of_all_numbers = 0                 # сумата на всички числа
max_number = -sys.maxsize      # най-колямото число в Python, например 2147483647

for num in range(numbers):         # range(1, numbers + 1)
    current_number = int(input())
    sum_of_all_numbers += current_number
    if current_number > max_number:   # най-голямото число, което да се яви равно на сумата на останалите числа
        max_number = current_number

if max_number == sum_of_all_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    sum_other_numbers = sum_of_all_numbers - max_number
    difference = abs(max_number - (sum_of_all_numbers - max_number))
    print("No")
    print(f'Diff = {difference}')