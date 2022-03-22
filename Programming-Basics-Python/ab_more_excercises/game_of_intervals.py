number_of_games = int(input())

total_numbers = 0

invalid_number = 0
numbers_to_9 = 0
numbers_to_19 = 0
numbers_to_29 = 0
numbers_to_39 = 0
numbers_to_50 = 0


for game in range(1, number_of_games + 1):
    number = int(input())

    if number < 0 or number > 50:
        invalid_number += 1
        total_numbers /= 2
    elif number >= 0 and number < 10:
        numbers_to_9 +=1
        total_numbers += 0.20 * number
    elif number >= 10 and number < 20:
        numbers_to_19 += 1
        total_numbers += 0.30 * number
    elif number >= 20 and number < 30:
        numbers_to_29 += 1
        total_numbers += 0.40 * number
    elif number >= 30 and number < 40:
        numbers_to_39 += 1
        total_numbers += 50
    elif number >= 40 and number <= 50:
        numbers_to_50 += 1
        total_numbers += 100

percent_invalid = invalid_number / number_of_games * 100
percent_to_10 = numbers_to_9 / number_of_games * 100
percent_to_20 = numbers_to_19 / number_of_games * 100
percent_to_30 = numbers_to_29 / number_of_games * 100
percent_to_40 = numbers_to_39 / number_of_games * 100
percent_to_50 = numbers_to_50 / number_of_games * 100

print(f"{total_numbers:.2f}")
print(f"From 0 to 9: {percent_to_10:.2f}%")
print(f"From 10 to 19: {percent_to_20:.2f}%")
print(f"From 20 to 29: {percent_to_30:.2f}%")
print(f"From 30 to 39: {percent_to_40:.2f}%")
print(f"From 40 to 50: {percent_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")