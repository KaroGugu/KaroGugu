type_of_movie = input()
number_rows = int(input())
number_colons = int(input())

total_seats = number_rows * number_colons

price_of_ticket = 0

if type_of_movie == "Premiere":
    price_of_ticket = 12
elif type_of_movie == "Normal":
    price_of_ticket = 7.50
else:                             # elif type_of_movie == "Discount"
    price_of_ticket = 5

total_price = total_seats * price_of_ticket
print(f'{total_price:.2f}')