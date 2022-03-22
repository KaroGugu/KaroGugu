numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for num in range(numbers):            # range(1, numbers + 1)
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number < 400:         # 200 <= current_number <= 399
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    else:                             # elif current_number >= 800
        p5 += 1

# колко пъти Р1 се е срещнало в диапазона - в процент
print(f"{p1 / numbers * 100:.2f}%")
print(f"{p2 / numbers * 100:.2f}%")
print(f"{p3 / numbers * 100:.2f}%")
print(f"{p4 / numbers * 100:.2f}%")
print(f"{p5 / numbers * 100:.2f}%")