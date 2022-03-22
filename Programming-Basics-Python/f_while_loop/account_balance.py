inpt = input()               # направите определен брой вноски

balance = 0.0               # колко общо пари има в сметката

while inpt != "NoMoreMoney":      # до получаване на команда  "NoMoreMoney "
    amount = float(inpt)         # На всеки ред ще получавате сумата, която трябва да внесете в сметката
    if amount < 0:               # Ако получите число по-малко от 0 - програмата да приключи
        print("Invalid operation!")
        break

    balance += amount               # При всяка получена сума на конзолата трябва да се извежда "Increase: "
                                    # + сумата и тя да се прибавя в сметката
    print(f"Increase: {amount:.2f}")
    inpt = input()

print(f"Total: {balance:.2f}")     # общата сума в сметката