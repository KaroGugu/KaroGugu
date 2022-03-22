number_of_people = int(input())
state_of_list = [int(x) for x in input().split(' ')]

capacity = 4

free_space = len(state_of_list) * 4 - sum(state_of_list)

if number_of_people > free_space:
    print(f"There isn't enough space! {number_of_people - free_space} people in a queue!")
    print(' '.join([str(capacity)] * len(state_of_list)))

elif number_of_people == free_space:
    print(' '.join([str(capacity)] * len(state_of_list)))

else: 
    for i in range(len(state_of_list)):
        while number_of_people > 0:
            if state_of_list[i] < capacity:
                state_of_list[i] += 1
                number_of_people -= 1
            else:
                break
        else: 
            break
    print("The lift has empty spots!")
    print(' '.join(str(i) for i in state_of_list))