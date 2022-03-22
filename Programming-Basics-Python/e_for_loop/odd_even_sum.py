numbers = int(input())                         # броя числа, които въвеждаме / циклите

sum_odd = 0
sum_even = 0

for num in range(numbers):                   # индекса / позицията на числото от поредицата, а не самото число
    current_number = int(input())

    if num % 2 == 0:                         # индекса / позицията на числото от поредицата, а не самото число
        sum_even += current_number
    else:
        sum_odd += current_number

if sum_odd == sum_even:
    print("Yes")
    print(f"Sum = {sum_even}")

else:
    diff = abs(sum_odd - sum_even)
    print("No")
    print(f"Diff = {diff}")