most_powerful_word = ""
most_powerful_word_score = 0

while True:                                       # До получаване на команда "End of words"
    word = input()

    if word == "End of words":
        break

    current_counter_of_chars = 0

    for ch in word: # За да се открие силата на всяка една, трябва да се намери сборът от ASCII стойностите на символите
       current_counter_of_chars += ord(ch)     # стойностите на символите от ASCII таблицата

# Ако започва с гласна буква - 'a', 'e', 'i', 'o', 'u', 'y' (или техните еквивалентни главни букви)
    # полученият сбор трябва да се умножи по дължината на думата
    if word[0].lower() in "aeiouy":
        current_counter_of_chars = current_counter_of_chars * len(word)
    else: # раздели на дължината и да се закръгли до най-близкото цяло число надолу
        current_counter_of_chars = int(current_counter_of_chars / len(word))
        # с int взимаме всичко преди десетичната запетя


    if current_counter_of_chars > most_powerful_word_score:
        most_powerful_word = word
        most_powerful_word_score = current_counter_of_chars

print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_score}")