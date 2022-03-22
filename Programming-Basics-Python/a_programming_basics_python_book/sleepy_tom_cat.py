free_days = int(input())

working_days = 365 - free_days

play_in_free_days = free_days * 127
play_in_working_days = working_days * 63
total_play_minutes = play_in_free_days + play_in_working_days

# нормата за игра на Том е 30 000 минути в година
difference = abs(total_play_minutes - 30000)
hours = difference // 60
minutes = difference % 60

if total_play_minutes >= 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")