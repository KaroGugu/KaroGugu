n = int(input("n = "))
min_number = 10000000000000

for i in range(n):
    number = int(input())
    if number < min_number:
        min_number = number

print("min = " + str(min_number))