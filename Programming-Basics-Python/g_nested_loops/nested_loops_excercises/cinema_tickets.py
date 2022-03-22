command = input()               # командата "Finish" или име на филма

students_tickets_counter = 0
standard_tickets_counter = 0
kid_tickets_counter = 0
total_tickets_counter = 0

while command != "Finish":
    movie_name = command
    free_seats = int(input())
    total_places = free_seats
    sold_tickets = 0
    while free_seats > 0:
        ticket_type = input()       # "End" или "student"/ "standard"/ "kid"
        if ticket_type == "End":
            break                   # прекъсва само while free_seats цикъла
        elif ticket_type == "student":
            students_tickets_counter += 1
        elif ticket_type == "standard":
            standard_tickets_counter += 1
        elif ticket_type == "kid":      # else:
            kid_tickets_counter += 1

        free_seats -= 1
        sold_tickets += 1
        total_tickets_counter += 1

    percent_full = sold_tickets / total_places * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    command = input()

print(f"Total tickets: {total_tickets_counter}")
print(f"{(students_tickets_counter / total_tickets_counter * 100):.2f}% student tickets.")
print(f"{(standard_tickets_counter / total_tickets_counter * 100):.2f}% standard tickets.")
print(f"{(kid_tickets_counter / total_tickets_counter * 100):.2f}% kids tickets.")