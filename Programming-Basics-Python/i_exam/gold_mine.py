number_of_locations = int(input())

for location in range(number_of_locations):
    target_gold_per_day = float(input())
    days_per_location = int(input())

    gold = 0

    for day in range(days_per_location):
        gold_per_day = float(input())

        gold += gold_per_day

    average_gold = gold / days_per_location
    if average_gold >= target_gold_per_day:
        pass
    else:
        pass

    if average_gold >= target_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
        continue
    else:
        diff = abs(target_gold_per_day - average_gold)
        print(f"You need {diff:.2f} gold.")

    if average_gold >= target_gold_per_day:
        break