max_first_number = int(input())
max_second_number = int(input())
max_third_number = int(input())

for first_number in range(2, max_first_number + 1, 2):      # четна цифра
    for second_number in range(2, max_second_number + 1):   # просто число в диапазона [2...7]
        for third_number in range(2, max_third_number + 1, 2):
            if second_number == 2 or second_number == 3 or second_number == 5 or second_number == 7:
                print(f"{first_number} {second_number} {third_number}")