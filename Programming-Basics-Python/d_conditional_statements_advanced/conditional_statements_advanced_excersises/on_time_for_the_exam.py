hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_or_arriving = int(input())
minutes_of_arriving = int(input())

time_of_exam = hour_of_exam * 60 + minutes_of_exam              # hours into minutes = * 60
time_of_arriving = hour_or_arriving * 60 + minutes_of_arriving


if time_of_arriving > time_of_exam:
    print("Late")

elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print("On Time")

else:                              #elif time_of_arriving < time_of_exam
    print("Early")

# Ако студентът пристига с поне минута разлика от часа на изпита
difference = abs(time_of_exam - time_of_arriving)         # minutes
hours = difference // 60
minutes = difference % 60

if time_of_exam - 60 < time_of_arriving < time_of_exam:   # по-рано с по-малко от час # с поне минута преди изпита
    print(f"{difference} minutes before the start")
elif time_of_arriving <= time_of_exam - 60:               # подраняване с 1 час или повече
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
    # print(f"{hours}:{hours:2d} hours before the start")

elif time_of_exam < time_of_arriving < time_of_exam + 60:     # закъснение под час
    print(f"{difference} minutes after the start")

elif time_of_arriving >= time_of_exam + 60:          # закъснение от 1 час или повече
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")
