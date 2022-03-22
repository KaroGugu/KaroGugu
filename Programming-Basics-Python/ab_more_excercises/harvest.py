from math import floor, ceil
squire_meters = int(input())
kg_grape_for_sq_meter = float (input())
liters_wine = int(input())
number_workers = int(input())

total_kg_grape = squire_meters * kg_grape_for_sq_meter
grape_for_wine = total_kg_grape * 0.40 / 2.5
left_wine = abs(grape_for_wine - liters_wine)


if grape_for_wine >= liters_wine:
    wine_for_worker = left_wine / number_workers
    print(f"Good harvest this year! Total wine: {floor(grape_for_wine)} liters.")
    print(f"{ceil(left_wine)} liters left -> {ceil(wine_for_worker)} liters per person.")

else:
    print(f"It will be a tough winter! More {floor(left_wine)} liters wine needed.")