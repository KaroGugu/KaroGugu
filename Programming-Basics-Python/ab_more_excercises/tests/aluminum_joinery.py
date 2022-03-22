number_of_windows = int(input())
type_of_window = input()
delivery = input()
price = 0

if type_of_window == '90X130':
    price = 110 * number_of_windows
    if 30 < number_of_windows <= 60:
        price *= 0.95                  # 5% отстъпка
    elif number_of_windows > 60:
        price *= 0.92                 # 8% отстъпка
elif type_of_window == '100X150':
    price = 140 * number_of_windows
    if 40 < number_of_windows <= 80:
        price *= 0.94                 # 6% отстъпка
    elif number_of_windows > 80:
        price *= 0.90                 # 10% отстъпка            # price -= price * 0.10
elif type_of_window == '130X180':
    price = 190 * number_of_windows
    if 20 < number_of_windows <= 50:
        price -= price * 0.07         # 7% отстъпка
    elif number_of_windows > 50:
        price -= price * 0.12         # 12% отстъпка
elif type_of_window == '200X300':
    price = 250 * number_of_windows
    if 25 < number_of_windows <= 50:
        price -= price * 0.09         # 90% отстъпка
    elif number_of_windows > 50:
        price -= price * 0.14         # 14% отстъпка

if delivery == 'With delivery':
    price += 60
elif delivery == 'Without delivery':
    price = price

if number_of_windows <= 10:
    print('Invalid order')
elif number_of_windows > 99:
    price -= price * 0.04            # 4% отстъпка
    print(f"{price:.2f} BGN")
else:
    print(f"{price:.2f} BGN")