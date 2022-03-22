hour = int(input())
minutes = int(input())
minutes += 15                                    # minutes = minutes + 15

# hour *= 60
# total_time = hour + minutes

hour += minutes // 60  # 1 h = 60 min      # if minutes >= 60    hours += 1
minutes %= 60  # minutes = minutes % 60

if hour > 23:  # if hour == 24
    hour = 0  # hour -= 24

if minutes <= 9:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')
