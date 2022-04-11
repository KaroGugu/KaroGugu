bands = {}
total_time = 0

command = input()

while not command == "Start!":
    split_command = command.split("; ")

    if split_command[0] == "Add":
        band_name, member = split_command[1:]
        bands[band_name] = band_name
        bands[band_name]= member

        if band_name in bands:
            if member not in bands:
                bands[band_name] = member

    elif split_command[0] == "Play":
        band_name = split_command[1]
        time = int(split_command[2])

        if band_name not in bands:
            bands[band_name] = band_name
            bands[band_name] = time
        else:
            total_time += time

    command = input()

print(f"Total time: {total_time}")

for key, value in bands.items():
    print(f"{key} -> {value}")