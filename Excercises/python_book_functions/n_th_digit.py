number = int(input())
index = int(input())

def nth_digit(number, index):
    return abs(number) // (10**(index-1)) % 10

print(nth_digit(number, index))

