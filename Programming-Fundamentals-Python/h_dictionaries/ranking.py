contest_command = input()  # some lines of input in format "{contest}:{password}" until you receive "end of contests"

contests_dict = {}

while contest_command != "end of contests":
    contest, password = contest_command.split(":")
    contests_dict[contest] = password  # Save that data because you will need it later

    contest_command = input()


submission_command = input()  # receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}"
users_dict = {}

while submission_command != "end of submissions":
    (contest, password, username, points) = submission_command.split("=>")

    if contest in contests_dict and contests_dict[contest] == password:
        # if the contest is valid (if you received it in the first type of input)
        # if the password is correct for the given contest
        if username not in users_dict:
            users_dict[username] = {}  # save the user with the contest they take part

        if contest not in users_dict[username]:  # save the points the user has in the given contest
            users_dict[username][contest] = int(points)
        else:
            if users_dict[username][contest] < int(points):  # update the points - if the new ones are more
                users_dict[username][contest] = int(points)

    submission_command = input()

best_user = ""  # you should print the info for the user with the most points
best_points = 0

for user in users_dict.keys():
    total_points = sum(users_dict[user].values())
    if total_points > best_points:
        best_points = total_points
        best_user = user

print(f"Best candidate is {best_user} with total {best_points} points.")

# all students ordered by their names.
print("Ranking:")
for user in sorted(users_dict.keys()):  # For each user print each contest with the points in descending order.
    print(user)
    for contest, points in sorted(users_dict[user].items(), key=lambda cp: cp[1], reverse=True):
        print(f"#  {contest} -> {points}")