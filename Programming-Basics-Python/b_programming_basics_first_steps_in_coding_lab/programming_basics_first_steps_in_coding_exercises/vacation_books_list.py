pages_of_a_book = int(input())                   # грешка в документа => да работим с реални числа
pages_per_hour = int(input())
day_for_a_book = int(input())

hours_for_reading = pages_of_a_book / pages_per_hour

time_per_day = hours_for_reading // day_for_a_book                    # целочислено деление

print(time_per_day)

# или    time_per_day = hours_for_reading / day_for_a_book
# print(int(time_per_day))         # т.е. взима само цялото число