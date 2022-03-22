numbers = int(input())

sum_even_numbers = 0
sum_odd_numbers = 0

for num in range(1, numbers + 1):
    number = int(input())
    if num % 2 == 0:
        sum_even_numbers += number
    else:
        sum_odd_numbers += number

difference = abs(sum_even_numbers - sum_odd_numbers)

if difference == 0:
    print("Yes")
    print(f"Sum = {sum_even_numbers}")
else:
    print("No")
    print(f"Diff = {difference}")