days = int(input())
daily_plunder = int(input())
target = float(input())

gained_plunder = 0

for day in range(1, days + 1):
    gained_plunder += daily_plunder

    if day % 3 == 0:
        gained_plunder += 0.50 * daily_plunder

    if day % 5 == 0:
        gained_plunder -= 0.30 * gained_plunder

percent = (gained_plunder / target) * 100

if gained_plunder >= target:
    print(f"Ahoy! {gained_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {percent:.2f}% of the plunder.")