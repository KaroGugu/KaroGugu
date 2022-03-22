

def sum_numbers(num_1:int, num_2:int):
    sum = num_1 + num_2

    return sum      # num1 + num2

def substract(sum: int, num_3: int):
    difference = sum - num_3

    return difference      # sum_1 - num3

def add_and_subtract(num1: int, num2: int, num3:int):
    sum_1 = sum_numbers(num_1, num_2)
    result = substract(sum_1, num_3)

    return result

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))