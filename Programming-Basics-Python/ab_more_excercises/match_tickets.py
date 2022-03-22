budget = float(input())
type_of_ticket = input()
number_of_people = int(input())

transport = 0
needed_money = 0
money_left = 0
ticket_price = 0

if type_of_ticket == 'Normal':
    ticket_price = 249.99
elif type_of_ticket == 'VIP':
    ticket_price = 499.99

needed_money = ticket_price * number_of_people

if number_of_people >= 1 and number_of_people <= 4:
    transport = budget * 0.75
    money_left = budget - transport
elif number_of_people >= 5 and number_of_people <=9:
    transport = budget * 0.60
    money_left = budget - transport
elif number_of_people >= 10 and number_of_people <= 24:
    transport = budget * 0.50
    money_left = budget - transport
elif number_of_people >= 25 and number_of_people <=49:
    transport = budget * 0.40
    money_left = budget - transport
elif number_of_people >= 50:
    transport = budget * 0.25
    money_left = budget - transport

difference = abs(needed_money - money_left)

if needed_money > money_left:
    print(f'Not enough money! You need {difference:.2f} leva.')
else:
    print(f'Yes! You have {difference:.2f} leva left.')