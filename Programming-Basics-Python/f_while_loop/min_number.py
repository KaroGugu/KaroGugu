import sys

min_number = sys.maxsize

while True:
    number = input()              # защото по някое време ще получим команда "Stop"

    if number == "Stop":
        break
    elif int(number) < min_number:
        min_number = int(number)

print(min_number)