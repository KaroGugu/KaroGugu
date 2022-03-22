n = int(input())
max_number = -10000000000000

for i in range (n):
    number = int(input())
    if number > max_number:
        max_number = number

print("max = " + str(max_number))