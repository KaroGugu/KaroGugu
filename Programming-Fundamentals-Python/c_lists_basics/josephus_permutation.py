people_in_the_circle = input().split()
person_executed = int(input())

final_list = []
counter = 0

index = 0
while len(people_in_the_circle) > 0:
    counter += 1

    if counter % person_executed == 0:
        final_list.append(people_in_the_circle.pop(index))
    else:
        index += 1

    if index >= len(people_in_the_circle):
        index = 0

print(str(final_list).replace(' ', '').replace('\'', ''))
