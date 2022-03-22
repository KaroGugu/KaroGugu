town = input()
type_of_packet = input()
vip = input()
days = int(input())

if days > 7:           # Ако клиентът е заявил престой повече от 7 дни, получава единия ден безплатно
    days -= 1

if not (town in ("Bansko", "Borovets") and type_of_packet in ("noEquipment", "withEquipment",)) and not (
        town in ("Varna", "Burgas") and type_of_packet in ("noBreakfast", "withBreakfast")):
    print(f'Invalid input!')

elif days < 1:
    print(f'Days must be positive number!')

else:
    if town == 'Bansko' or town == 'Borovets':
        if type_of_packet == 'withEquipment':
            price = 100 * days
            if vip == 'yes':
                price *= 0.9                   # 10%
        elif type_of_packet == 'noEquipment':
            price = 80 * days
            if vip == 'yes':
                price *= 0.95                 # 5%

    elif town == 'Varna' or town == 'Burgas':
        if type_of_packet == 'withBreakfast':
            price = 130 * days
            if vip == 'yes':
                price *= 0.88                 # 12%
        elif type_of_packet == 'noBreakfast':
            price = 100 * days
            if vip == 'yes':
                price *= 0.93                 # 7%

    print(f'The price is {price:.2f}lv! Have a nice time!')