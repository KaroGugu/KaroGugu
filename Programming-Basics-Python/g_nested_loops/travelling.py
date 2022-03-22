
current_sum = 0

while True:
    destination = input()
    if destination == "End":
        break

    budget = float(input())               # минималния бюджет, който ще е нужен за пътуването.
    current_sum = 0

    while budget > current_sum:
        save_sum = float(input())         # няколко суми, които Ани спестява
        current_sum += save_sum

        if current_sum >= budget:
            print(f"Going to {destination}!")
            break