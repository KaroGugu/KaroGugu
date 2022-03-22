charity_sum = int(input())
amount_is_enough = False
cs_count = 0
cc_count = 0
cs_amount = 0
cc_amount = 0
average_cs = 0
average_cc = 0

price = input()
count = 1
while price != "End":
    price = int(price)
    if count % 2 != 0 and price <= 100:
        cs_amount += price
        cs_count += 1
        average_cs = cs_amount / cs_count
        print("Product sold!")
    elif count % 2 == 0 and price >= 10:
        cc_amount += price
        cc_count += 1
        average_cc = cc_amount / cc_count
        print("Product sold!")
    else:
        print("Error in transaction!")
    if cs_amount + cc_amount >= charity_sum:
        amount_is_enough = True
        break
    price = input()
    count += 1

if amount_is_enough:
    print(f'Average CS: {average_cs:.2f}')
    print(f'Average CC: {average_cc:.2f}')
else:
    print("Failed to collect required money for charity.")