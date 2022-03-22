first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time

# сумарното им време във формат "минути:секунди".
minutes = total_time // 60
# 1 min = 60 sec         500 sec // 60 = 8min + x sec
seconds = total_time % 60
# seconds = total_time - minutes * 60

# Секундите да се изведат с водеща нула (2  "02")
if seconds < 10:  # при едно числени cекундите; <= 9
    print(f'{minutes}:0{seconds}')

else:
    print(f'{minutes}:{seconds}')
