period = int(input())

water_per_month = 20
internet_per_month = 15
other_bills = 0
electricity_for_period = 0

for month in range(period):
    electricity_per_month = float(input())
    electricity_for_period += electricity_per_month
    water_for_period = period * water_per_month
    internet_for_period = period * internet_per_month
    other_bills += (electricity_per_month + water_per_month + internet_per_month) + \
                   (0.20 * (electricity_per_month + water_per_month + internet_per_month))


average_per_month = (electricity_for_period + water_for_period + internet_for_period + other_bills) / period

print(f"Electricity: {electricity_for_period:.2f} lv")
print(f"Water: {water_for_period:.2f} lv")
print(f"Internet: {internet_for_period:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average_per_month:.2f} lv")
