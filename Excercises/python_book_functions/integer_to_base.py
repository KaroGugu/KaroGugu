number = int(input())
base = int(input())

def integer_to_base (number, base):
    result = ""
    while number != 0:
        remain = number % base
        result += remain
        result += number / base

        return result

print(integer_to_base(number, base))