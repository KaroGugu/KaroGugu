old_record = float(input())
distance = float(input())
time_per_meter = float(input())

delay = (distance // 15) * 12.5                          # забавяне на всеки 15 м. с 12.5 секунди
      # int(distance / 15)
      # floor(disctance / 15)              # from math import floor

total_time = (distance * time_per_meter) + delay

if total_time < old_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds_more = total_time - old_record                 # abs(old_record - total_time)
    print(f'No, he failed! He was {seconds_more:.2f} seconds slower.')
