name_of_company = input()
number_of_tickets_for_adults = int(input())
number_of_tickets_for_kids = int(input())
price_of_ticket_for_adult = float(input())
tax = float(input())

price_of_ticket_for_kid = 0.30 * price_of_ticket_for_adult
price_of_ticket_for_adult += tax
price_of_ticket_for_kid += tax
profit_for_company = 0.20

total_price_of_tickets = (number_of_tickets_for_kids * price_of_ticket_for_kid) + \
                         (number_of_tickets_for_adults * price_of_ticket_for_adult)

profit_for_company = 0.20 * total_price_of_tickets

print(f"The profit of your agency from {name_of_company} tickets is {profit_for_company:.2f} lv.")
