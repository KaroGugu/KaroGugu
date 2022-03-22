kilometers = int(input())
word_day_or_night = input()

# taxi = 0.70         # day = 0.79                # night = 0.90
# bus                 # day / night = 0.09                                # min distance = 20
# train               # day / night = 0.06                                # min distance = 100

if kilometers < 20:
    if word_day_or_night == "day":
       taxi = 0.70 + (kilometers * 0.79)
       print(f"{taxi:.2f}")
    else:
        taxi = 0.70 + (kilometers * 0.90)
        print(f"{taxi:.2f}")

elif 20 <= kilometers < 100:
    bus = 0.09 * kilometers
    print(f'{bus:.2f}')

else:
    train = 0.06 * kilometers
    print(f'{train:.2f}')