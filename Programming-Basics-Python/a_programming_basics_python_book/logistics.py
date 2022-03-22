counts_of_loads = int(input())

sum_of_tons = 0
microbus_tons = 0
truck_tons = 0
train_tons = 0

for ton in range(1, counts_of_loads + 1):
    tons = int(input())
    if tons <= 3:
        microbus_tons += tons
    elif tons <= 11:
        truck_tons += tons
    elif tons >= 12:
        train_tons += tons

sum_of_tons += microbus_tons + truck_tons + train_tons

microbus_price = microbus_tons * 200
truck_price = truck_tons * 175
train_price = train_tons * 120
total_price = microbus_price + truck_price + train_price
average_price = total_price / sum_of_tons

percent_microbus_tons = microbus_tons / sum_of_tons * 100
percent_truck_tons = truck_tons / sum_of_tons * 100
percent_train_tons = train_tons / sum_of_tons * 100

print(f"{average_price:.2f}")
print(f"{percent_microbus_tons:.2f}%")
print(f"{percent_truck_tons:.2f}%")
print(f"{percent_train_tons:.2f}%")