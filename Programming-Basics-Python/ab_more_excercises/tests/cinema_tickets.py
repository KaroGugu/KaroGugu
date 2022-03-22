movie_name = input()              # командата "Finish" / име на филма

student_ticket = 0
standard_ticket = 0
kid_ticket = 0
total_movie_tickets = 0

while movie_name != "Finish":
    free_seats = int(input())     # свободните места в салона за всяка прожекция
    for seat in range(free_seats):    # За всеки филм да се чете Типа на закупения билет
        ticket_type = input()        # командата "End" / Типа на закупения билет
        if ticket_type == "End":
            break
        if ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1
        total_movie_tickets += 1                            # Общо билета

    percent_full = total_movie_tickets / free_seats * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    total_movie_tickets = 0
    movie_name = input()

total_tickets = student_ticket + standard_ticket + kid_ticket       # Общо закупените билети за всички филми
percent_standard_ticket = standard_ticket / total_tickets * 100
percent_student_ticket = student_ticket / total_tickets * 100
percent_kid_ticket = kid_ticket / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student_ticket:.2f}% student tickets.")
print(f"{percent_standard_ticket:.2f}% standard tickets.")
print(f"{percent_kid_ticket:.2f}% kids tickets.")
