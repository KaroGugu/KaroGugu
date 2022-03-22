number = input()

num = str(number)

sorted_digits = sorted(num, reverse=True)
for index, digit in enumerate(sorted_digits):
    print(digit, end="")
