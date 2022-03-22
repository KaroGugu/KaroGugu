targets_value = list(map(int,input().split()))

shot_target = 0
counter = 0

command = input()
while command != "End":
    index_of_target = int(command)
    if index_of_target < len(targets_value):  # you need to shoot the target on that index, if it is possible
        if targets_value[index_of_target] != -1: # you can't shoot a target, which is already shot
            shot_target = targets_value[index_of_target]
            targets_value[index_of_target] = -1  # Every time you shoot a target, its value becomes -1
            counter += 1   # and it is considered shot

        for i in range(len(targets_value)):
            if targets_value[i] > shot_target and targets_value[i] != -1:
                # Reduce all the other targets, which have greater values than your current target, with its value
                targets_value[i] -= shot_target
            elif targets_value[i] <= shot_target and targets_value[i] != -1:
                # Increase all the other targets, which have less than or equal value to the shot target, with its value
                targets_value[i] += shot_target

    command = input()

targets_value = str(targets_value).replace(",", "").replace("[", "").replace("]", "")
print(f"Shot targets: {counter} -> {targets_value}")