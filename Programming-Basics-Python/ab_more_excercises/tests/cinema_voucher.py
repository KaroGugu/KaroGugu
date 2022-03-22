voucher = int(input())

ticket_counter = 0
others_counter = 0
price = 0                 # цена на покупката

command = input()           # името на покупките, които желае, докато не въведе "End"
while command != "End":
    voucher -= price
    if len(command) > 8:              # Ако името на покупката съдържа повече от 8 символа, то тя е билет за филм
        price = ord(command[0]) + ord(command[1])  # цена = сумата на ASCII символите от първите ѝ два символа
        if voucher >= price:
            ticket_counter += 1

    else:
        price = ord(command[0])  # цена = стойността на първия ASCII символ в името
        if voucher >= price:
            others_counter += 1

    if voucher < price:           # покупка, чиято стойност е по-голяма от останалата сума на ваучера
        break

    command = input()

print(ticket_counter)
print(others_counter)