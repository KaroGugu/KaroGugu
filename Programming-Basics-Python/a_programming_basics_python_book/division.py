numbers = int(input())

divisible_2 = 0
divisible_3 = 0
divisible_4 = 0

for num in range(numbers):
    current_number = int(input())
    if current_number % 2 == 0:
        divisible_2 += 1
    if current_number % 3 == 0:
        divisible_3 += 1
    if current_number % 4 == 0:
        divisible_4 += 1

percent_p1 = divisible_2 / numbers * 100
percent_p2 = divisible_3 / numbers * 100
percent_p3 = divisible_4 / numbers * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")