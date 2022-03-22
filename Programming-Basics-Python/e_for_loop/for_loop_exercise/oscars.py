name_of_actor = input()
academy_points = float(input())
number_of_jury = int(input())

total_points = academy_points

for current_grade in range(number_of_jury):            # range(1, number_of_jury +1)
    current_name = input()
    current_points = float(input())
    current_final_points = (len(current_name) * current_points) / 2
    total_points += current_final_points
    if total_points > 1250.5:
        break                                    # is_nominated = True   # break
if total_points > 1250.5:                        #if is_nominataed == True
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {name_of_actor} you need {difference:.1f} more!")