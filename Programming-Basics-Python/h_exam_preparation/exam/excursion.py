number_of_people = int(input())
number_of_nights = int(input())
number_of_transport_cards = int(input())
number_of_tickets = int(input())

price_per_night = 20
price_transport_card = 1.60
price_ticket = 6

sum_per_person_for_all_nights = number_of_nights * price_per_night
sum_per_person_for_transport_cards = number_of_transport_cards * price_transport_card
sum_per_person_for_ticket = number_of_tickets * price_ticket

total_sum_for_one_person = sum_per_person_for_all_nights + sum_per_person_for_transport_cards + sum_per_person_for_ticket
total_sum_for_all_people = number_of_people * total_sum_for_one_person

total_sum = total_sum_for_all_people + (0.25 * total_sum_for_all_people)

print(f"{total_sum:.2f}")

