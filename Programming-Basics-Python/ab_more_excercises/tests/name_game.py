command = input()   # До получаване на командата "Stop" / Име на играча с дължина n

score = 0
best_score = 0
best_player = ""

while command != "Stop":

    for letter in command:   # за всяка една буква от името си написва по едно цяло число
        number = int(input())

        if number == ord(letter):  # ако числото съвпада с ASCII стойността на съответната буква
            score += 10
        elif number != ord(letter):
            score += 2

    if score >= best_score:        # Победител е играчът с най-много точки в края на играта
        best_score = score
        best_player = command
    score = 0

    command = input()

print(f"The winner is {best_player} with {best_score} points!")