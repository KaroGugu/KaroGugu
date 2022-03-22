numbers = int(input())

previous_sum = 0
max_difference = 0

for num in range(numbers):
    first_number = int(input())
    second_number = int(input())
    new_sum = first_number + second_number
    if previous_sum != 0 and previous_sum != new_sum:   # дали всички двойки имат еднаква стойност
        difference = abs(new_sum - previous_sum)        # максималната разлика между две последователни двойки
        if difference > max_difference:
            max_difference = difference

    previous_sum = new_sum

if max_difference == 0:                   # всички двойки имат еднаква стойност
    print(f"Yes, value={new_sum}")
else:
    print(f"No, maxdiff={max_difference}")