packets_of_pens = int(input())
packets_of_markers = int(input())
liters_of_liquid = int(input ())

discount = int (input())

#добавям си като напомняне цените, които са ми дадени в условието
price_of_pen = 5.80
price_of_markers = 7.20
price_of_liquid = 1.20


total_sum = packets_of_pens * price_of_pen + packets_of_markers * price_of_markers + \
            liters_of_liquid * price_of_liquid

#за да напраея обаче отстъпката като % трябва да я разделя на 100
discount = discount / 100                           # discount /= 100

total_sum = total_sum - (total_sum * discount)

print(total_sum)