number_of_days = int(input())
number_of_hours = int(input())

cost_for_all_period = 0

for day in range(1, number_of_days + 1):
    current_cost = 0
    for hour in range(1, number_of_hours + 1): # Брой часове за всеки един от дните
        if day % 2 == 0 and hour % 2 != 0:       # За всеки четен ден и нечетен час, паркингът таксува 2.50 лева
            current_cost += 2.50
            cost_for_all_period += 2.50
        elif day % 2 == 1 and hour % 2 == 0:     # Във всеки нечетен ден и четен час таксата е 1.25 лева
            current_cost += 1.25
            cost_for_all_period += 1.25
        else:
            current_cost += 1
            cost_for_all_period += 1            # във всички останали случаи се заплаща 1 лев

    print(f"Day: {day} - {current_cost:.2f} leva")   # между двата фор-цикъл винаги ще го принтира

print(f"Total: {cost_for_all_period:.2f} leva")