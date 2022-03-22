first_number = int(input())
second_number = int(input())
third_number = int(input())

minus_counter = 0

if first_number < 0:
    minus_counter += 1
if second_number < 0:
    minus_counter += 1
if third_number < 0:
    minus_counter += 1

multiplication = first_number * second_number * third_number
if multiplication == 0:
    print("zero")
elif minus_counter % 2 == 0:
    print("positive")
else:
    print("negative")