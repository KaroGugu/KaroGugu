target_minutes = int(input())
target_seconds = int(input())
meters_tunnel = float(input())
seconds_Martin_per_100_meters = int(input())

number_of_delays = meters_tunnel // 120   # на всеки 120 метра неговото време намаля с 2.5 секунди.
total_delay_time = number_of_delays * 2.5

target_minutes_into_seconds = (target_minutes * 60) + target_seconds

time_Martin_in_seconds = (meters_tunnel / 100) * seconds_Martin_per_100_meters - total_delay_time

if round(time_Martin_in_seconds, 3) <= target_minutes_into_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_Martin_in_seconds:.3f}.")

elif round(time_Martin_in_seconds, 3) > target_minutes_into_seconds:
    diff = abs(time_Martin_in_seconds - target_minutes_into_seconds)
    print(f"No, Marin failed! He was {diff:.3f} second slower.")