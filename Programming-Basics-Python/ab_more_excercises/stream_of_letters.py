import string

count_c = 0
count_o = 0
count_n = 0
secret_word = ''               # тайна команда от три букви – "c", "o" и "n"
final_word = ""
command = input()

while command != "End":
    if command in string.ascii_letters:
        if command == "c" and count_c == 0:       # При първото получаване на една от тези букви,
                                                  # тя се маркира като срещната, но не се запазва в думата
            count_c += 1
        elif command == "o" and count_o == 0:
            count_o += 1
        elif command == "n" and count_n == 0:
            count_n += 1
        else:
            secret_word += command

        if count_c == 1 and count_o == 1 and count_n == 1:  # След като са налични и трите символа от командата,
                                                            # се печата думата и интервал " "
            final_word += secret_word + " "
            count_c, count_n, count_o = 0, 0, 0
            secret_word = ""                                # Започва се нова дума, която по същия начин чака тайната команда,
                                                     # за да бъде отпечатана
    command = input()

print(final_word)
