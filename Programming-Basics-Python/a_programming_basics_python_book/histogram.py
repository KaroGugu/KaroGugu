numbers = int(input())              # броя редове с числа, които ще ни бъдат подадени

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for num in range(numbers):
    current_number = int(input())          # На следващите n реда стои по едно цяло число

    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

percent_p1 = p1 / numbers * 100
percent_p2 = p2 / numbers * 100
percent_p3 = p3 / numbers * 100
percent_p4 = p4 / numbers * 100
percent_p5 = p5 / numbers * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")