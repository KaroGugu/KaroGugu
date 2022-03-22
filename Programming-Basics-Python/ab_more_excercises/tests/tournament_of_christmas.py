days = int(input())

days_won = 0
total_money = 0

for day in range(days):      # Всеки ден получавате имена на игри до команда "Finish
    command = input()        # имена на игри / команда "Finish
    games_won = 0
    games_lost = 0
    daily_money = 0         # колко пари сте спечелили на края на деня

    while command != "Finish":
        game = input()          # имена на игри
        if game == "win":
            daily_money += 20
            games_won += 1
        elif game == "lose":
            games_lost += 1

        command = input()

    if games_won > games_lost:      # повече спечелени игри, отколкото загубени – вие сте победители този ден
        daily_money *= 1.1          # увеличавате парите от деня с 10%
        days_won += 1

    total_money += daily_money

if days < 2 * days_won:   # приключване на турнира ако през повечето дни сте били победители печелите турнира
                          # т.е. повечето от половината дни са спечелени
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")