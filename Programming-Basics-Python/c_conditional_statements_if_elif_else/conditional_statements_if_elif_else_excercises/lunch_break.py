from math import ceil
name_of_movie = input()
time_for_movie = int(input())
time_for_break = int(input())

time_for_lunch = time_for_break / 8
time_for_relax = time_for_break / 4

free_time = time_for_break - time_for_lunch - time_for_relax

needed_time_for_movie = ceil(abs(free_time - time_for_movie))

if free_time >= time_for_movie:
    print(f'You have enough time to watch {name_of_movie} and left with {needed_time_for_movie} minutes free time.')

else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {needed_time_for_movie} more minutes.")