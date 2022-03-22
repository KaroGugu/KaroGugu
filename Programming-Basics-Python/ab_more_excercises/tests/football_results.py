first_match = input()
second_match = input()
third_match = input()

win_counter = 0
lose_counter = 0
draw_counter = 0

# Отборът винаги е домакин, следователно първата цифра от резултата съответства на головете вкарани от него

if ord(first_match[0]) > ord(first_match[2]):  # стойностите на елемент от текст - на първи и трети елемент
    win_counter += 1
elif ord(first_match[0]) < ord(first_match[2]):
    lose_counter += 1
elif ord(first_match[0]) == ord(first_match[2]):
    draw_counter += 1

if ord(second_match[0]) > ord(second_match[2]):
    win_counter += 1
elif ord(second_match[0]) < ord(second_match[2]):
    lose_counter += 1
else: # elif ord(second_match[0]) == ord(second_match[2]):
    draw_counter += 1

if ord(third_match[0]) > ord(third_match[2]):
    win_counter += 1
elif ord(third_match[0]) < ord(third_match[2]):
    lose_counter += 1
elif ord(third_match[0]) == ord(third_match[2]):
    draw_counter += 1

print(f"Team won {win_counter} games.")
print(f"Team lost {lose_counter} games.")
print(f"Drawn games: {draw_counter}")