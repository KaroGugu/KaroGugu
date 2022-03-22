number = int(input())

def print_sign(n):
    if n == 0:
        print(f"The number {n} is zero.")

    elif n > 0:
        print(f"The number {n} is positive.")

    elif n < 0:           # else:
        print(f"The number {n} is negative.")

print_sign(number)
