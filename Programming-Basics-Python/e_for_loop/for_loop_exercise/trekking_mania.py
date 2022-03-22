number_of_groups = int(input())

people_on_musala = 0
people_on_monblanc = 0
people_on_kilimanjaro = 0
people_on_k2 = 0
people_on_everest = 0

total_number_of_people = 0

for people in range(1, number_of_groups + 1):
    number_of_people_in_a_group = int(input())
    if number_of_people_in_a_group <= 5:
        people_on_musala += number_of_people_in_a_group
    elif number_of_people_in_a_group <= 12:
        people_on_monblanc += number_of_people_in_a_group
    elif number_of_people_in_a_group <= 25:
        people_on_kilimanjaro += number_of_people_in_a_group
    elif number_of_people_in_a_group <= 40:
        people_on_k2 += number_of_people_in_a_group
    else:                           #elif current_number_of_people > 40:
        people_on_everest +=number_of_people_in_a_group

total_number_of_people = people_on_musala + people_on_monblanc + people_on_kilimanjaro + people_on_k2 + people_on_everest

percent_people_on_musala = people_on_musala / total_number_of_people * 100
percent_people_on_monblanc = people_on_monblanc / total_number_of_people * 100
percent_people_on_kilimanjaro = people_on_kilimanjaro / total_number_of_people * 100
percent_people_on_k2 = people_on_k2 / total_number_of_people * 100
percent_people_on_everest = people_on_everest / total_number_of_people * 100

print(f"{percent_people_on_musala:.2f}%")
print(f"{percent_people_on_monblanc:.2f}%")
print(f"{percent_people_on_kilimanjaro:.2f}%")
print(f"{percent_people_on_k2:.2f}%")
print(f"{percent_people_on_everest:.2f}%")
