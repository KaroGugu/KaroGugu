sum = float(input())
#  за да не работим с дробни числ,а с плаваща запетая и да имаме банкерско закръгляне
sum = int(sum * 100)
coins_counter = 0

while sum > 0:
    if sum - 200 >= 0:
        coins_counter += 1
        sum -= 200
        continue
    elif sum - 100 >= 0:
        coins_counter += 1
        sum -= 100
        continue
    elif sum - 50 >= 0:
        coins_counter += 1
        sum -= 50
        continue
    elif sum - 20 >= 0:
        coins_counter += 1
        sum -= 20
        continue
    elif sum - 10 >= 0:
        coins_counter += 1
        sum -= 10
        continue
    elif sum - 5 >= 0:
        coins_counter += 1
        sum -= 5
        continue
    elif sum - 2 >= 0:
        coins_counter += 1
        sum -= 2
        continue
    elif sum - 1 >= 0:
        coins_counter += 1
        sum -= 1
        continue

print(coins_counter)