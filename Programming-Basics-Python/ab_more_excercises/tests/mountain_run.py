record = float(input())
distance = float(input())
second_per_meter = float(input())

delay = (distance // 50) * 30           # наклона на терена го забавя на всеки 50 м. с 30 секунди

time_climbing = distance * second_per_meter + delay

if time_climbing < record:
    print(f"Yes! The new record is {time_climbing:.2f} seconds.")
else:
    difference = abs(time_climbing - record)
    print(f"No! He was {difference:.2f} seconds slower.")