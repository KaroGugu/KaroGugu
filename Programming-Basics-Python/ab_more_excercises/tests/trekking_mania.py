number_of_groups = int(input())                     # броя на групите от катерачи

total_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k_2 = 0
everest = 0

for group in range(1, number_of_groups + 1):  # За всяка една група на отделен ред – броя на хората в групата
    number_of_people = int(input())

    if number_of_people > 0 and number_of_people <= 5:
        musala += number_of_people
    elif number_of_people >= 6 and number_of_people <= 12:
        monblan += number_of_people
    elif number_of_people <= 25:
        kilimandjaro += number_of_people
    elif number_of_people <= 40:
        k_2 += number_of_people
    elif number_of_people >= 41:
        everest += number_of_people

total_people += musala + monblan + kilimandjaro + k_2 + everest

percent_musala = musala / total_people * 100              # процентът изкачващи Мусала
percent_monblan = monblan / total_people * 100            # процентът изкачващи Монблан
percent_kilimandjaro = kilimandjaro / total_people * 100
percent_k_2 = k_2 / total_people * 100
percent_everest = everest / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_k_2:.2f}%")
print(f"{percent_everest:.2f}%")