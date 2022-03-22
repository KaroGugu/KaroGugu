distance = int(input())
word = input()

taxi = 0.70    # day = 0.79        # night = 0.90
bus = 0         # day = 0.09        # night = 0.09    # distance = min 20 km
train = 0       # day = 0.06        # night = 0.06    # distance = min 100 km

price = 0.00
taxi_price = 0.00

if word == "day":
    taxi_price = 0.79
else:
    taxi_price = 0.90

if distance < 20:
    price = 0.70 + distance * taxi_price
elif distance < 100:
    price = distance * 0.09
else:
    price = distance * 0.06

print(price)