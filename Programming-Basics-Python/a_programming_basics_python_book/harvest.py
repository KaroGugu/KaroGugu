from math import floor, ceil

loze = int(input())
grape_per_square = float(input())
needed_liters = int(input())
number_of_workers = int(input())

total_wine = loze * grape_per_square
wine = total_wine * 0.40 / 2.5  # От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино
                                         # За 1 литър вино са нужни 2,5 кг. грозде



diff = abs(needed_liters - wine)
wine_for_a_worker = diff / number_of_workers

if wine >= needed_liters:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(wine_for_a_worker)} liters per person.")

else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")