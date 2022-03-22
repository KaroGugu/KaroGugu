town = input()
volume_sells = float(input())

commissions = 0
condition = True             # При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

if town == "Sofia":
    if 0 <= volume_sells <= 500:
        commissions = volume_sells * 0.05
    elif 500 < volume_sells <= 1000:
        commissions = volume_sells * 0.07
    elif 1000 < volume_sells <= 10000:
        commissions = volume_sells * 0.08
    elif volume_sells > 10000:
        commissions = volume_sells * 0.12
    else:
        condition = False



elif town == "Varna":
    if 0 <= volume_sells <= 500:
        commissions = volume_sells * 0.045
    elif 500 < volume_sells <= 1000:
        commissions = volume_sells * 0.075
    elif 1000 < volume_sells <= 10000:
        commissions = volume_sells * 0.10
    elif volume_sells > 10000:
        commissions = volume_sells * 0.13
    else:
        condition = False


elif town == "Plovdiv":
    if 0 <= volume_sells <= 500:
        commissions = volume_sells * 0.055
    elif 500 < volume_sells <= 1000:
        commissions = volume_sells * 0.08
    elif 1000 < volume_sells <= 10000:
        commissions = volume_sells * 0.12
    elif volume_sells > 10000:
        commissions = volume_sells * 0.145
    else:
        condition = False

else:
    condition = False

if condition:
    print(f'{commissions:.2f}')
else:
    print("error")