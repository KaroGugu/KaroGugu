minutes = int(input())
number_of_walks = int(input())
calories = int(input())

cal_burned = 5

total_minutes_walking = minutes * number_of_walks
total_cal_burned = total_minutes_walking * cal_burned
walking_enough = 0.50 * calories

if total_cal_burned >= walking_enough:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_cal_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_cal_burned}.")
