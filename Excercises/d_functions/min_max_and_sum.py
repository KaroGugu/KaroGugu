numbers = input().split()

list = []

min_number = ""
max_number = ""
sum_numbers = 0

for num in numbers:
    current_number = int(num)
    list.append(current_number)

    min_number = min(list)
    max_number = max(list)
    sum_numbers += current_number

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")

