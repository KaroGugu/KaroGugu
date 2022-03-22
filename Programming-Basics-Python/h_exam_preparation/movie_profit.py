name_of_movie = input()
days = int(input())
number_of_tickets = int(input())
price_ticket = float(input())
percent_for_cinema = int(input())   # определен процент от общия приход остава за киното


sum_tickets_per_day = number_of_tickets * price_ticket
profit_for_all_period = days * sum_tickets_per_day
percent_tax = profit_for_all_period * (percent_for_cinema / 100)
total_profit_for_movie = profit_for_all_period - percent_tax

print(f"The profit from the movie {name_of_movie} is {total_profit_for_movie:.2f} lv.")

