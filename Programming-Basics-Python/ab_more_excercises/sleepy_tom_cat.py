free_days = int(input())

# workdays = по 63 минути на ден
# free_days = по 127 минути на ден
work_days = 365 - free_days
play_in_free_days = free_days * 127
play_in_work_days = work_days * 63

total_play = play_in_free_days + play_in_work_days

norm_for_play = 30000
difference = abs(norm_for_play - total_play)
hours = difference // 60
minutes = difference % 60

if total_play > norm_for_play:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')

else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')