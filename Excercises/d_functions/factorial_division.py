def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)


first_number = int(input())
second_number = int(input())

result = factorial(first_number) / factorial(second_number)
print(f"{result:.2f}")