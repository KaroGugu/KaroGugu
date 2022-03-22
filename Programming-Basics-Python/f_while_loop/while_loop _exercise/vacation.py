needed_money = float(input())
owned_money = float(input())

days_counter = 0               # броя изминали дни
spent_money_counter = 0           # броя последователни дни, в които Джеси харчи пари

while owned_money < needed_money and spent_money_counter < 5:
    # докато парите на Джеси са по-малко от парите, които са ѝ нужни за екскурзията
    # и броячът за последователните дни е по-малък от 5
    command = input()   #  spend или save, а вторият
    money = float(input()) #  парите, които Джеси е спестила или похарчила
    days_counter += 1

    if command == "save":
        owned_money += money       # прибавете спестените пари към нейните
        spent_money_counter = 0    # нулирайте брояча за поредните дни, в които харчи пари
    elif command == "spend":
        owned_money -= money
        spent_money_counter += 1   # извадете от нейните пари сумата която е похарчила
        if owned_money < 0:
            owned_money = 0        # парите на Джеси са станали по-малко от нула => останала без пари и има нула лева

if spent_money_counter == 5:       # дали Джеси е харчила пари в пет последователни дни
    print("You can't save the money.")
    print(days_counter)

if owned_money >= needed_money:    # дали Джеси е събрала парите
    print(f"You saved the money for {days_counter} days.")