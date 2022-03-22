command = input()
contests_dict = {}
users_dict = {}

while not command == "no more time":
    user_name, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contests_dict:
        contests_dict[contest] = {}
    if user_name not in contests_dict[contest]:
        contests_dict[contest][user_name] = points
    else:  # If the user has already participated in the contest
        if points > contests_dict[contest][user_name]:  # update their points if the new ones are more than the older
            contests_dict[contest][user_name] = points

    command = input()

for contest, users in contests_dict.items():
    for user_name, points in users.items():
        if user_name not in users_dict:
            users_dict[user_name] = points
        else:
            users_dict[user_name] += points

for contest, users in contests_dict.items():  # for each contest print the participants - by points in descending order
    print(f"{contest}: {len(users)} participants")
    count = 1
    for user_name, points in dict(sorted(users.items(), key=lambda kvp: (-kvp[1], kvp[0]))).items():
        print(f"{count}. {user_name} <::> {points}")
        count += 1

print("Individual standings:")

count_users = 1  # for every participant ordered by total points in descending order
for username, points in sorted(users_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{count_users}. {username} -> {points}")
    count_users += 1