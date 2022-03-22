first_numbers = int(input())
second_numbers = int(input())
third_numbers = int(input())

def smallest_number(a, b, c):
    smallest = min(a,b,c)
    result = smallest
    print(result)

smallest_number(first_numbers, second_numbers, third_numbers)