number_of_days = int(input())

sum_liters = 0
sum_degrees = 0

for day in range(1, number_of_days + 1):
    liters_rakia = float(input())
    degrees = float(input())

    sum_liters += liters_rakia
    degrees_per_day = liters_rakia * degrees
    sum_degrees += degrees_per_day

average_degrees = sum_degrees / sum_liters


print(f"Liter: {sum_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38.00:
    print("Not good, you should baking!")
elif average_degrees >= 38.00 and average_degrees <= 42.00:
    print("Super!")
elif average_degrees > 42.00:
    print("Dilution with distilled water!")