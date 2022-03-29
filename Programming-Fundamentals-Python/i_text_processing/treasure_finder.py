key = ''.join([x for x in input().split(' ')])  # a key (sequence of numbers separated by a space)

command = input()
while not command == "find":
    decrypted_message = command

    while len(key) < len(decrypted_message):  # If the length of the key sequence is less than the string sequence
        key += key  # you should continue looping from the beginning

    decrypted_coordinates = ''
    for i in range(len(decrypted_message)):    # You should loop through every string and
        # decrease the ASCII code of each character with a corresponding number of the key
        decrypted_coordinates += chr(ord(decrypted_message[i]) - int(key[i]))

    treasure = decrypted_coordinates[decrypted_coordinates.find('&') + 1:]
    treasure = treasure[:treasure.find('&')]
    coordinates = decrypted_coordinates[decrypted_coordinates.find('<') + 1:decrypted_coordinates.find('>')]

    command = input()

    print(f'Found {treasure} at {coordinates}')