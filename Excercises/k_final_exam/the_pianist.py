number_of_pieces = int(input())
pieces = {}

for i in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

command = input()

while not command == "Stop":
    split_command = command.split("|")
    if split_command[0] == "Add":
        piece, composer, key = split_command[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:  # add the given piece with the information about it to the other pieces
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif split_command[0] == "Remove":
        piece = split_command[1]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del pieces[piece]
            print(f"Successfully removed {piece}!")

    elif split_command[0] == "ChangeKey":
        piece, new_key = split_command[1:]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:  # change its key with the given one
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    command = input()

# print all pieces in your collection, sorted by their name and by the name of their composer in alphabetical order
# sorted_pieces = sorted(pieces.items(), key=lambda kvpt: (kvpt[0], kvpt[1]["composer"]))

for piece, command in pieces.items():
    print(f"{piece} -> Composer: {command['composer']}, Key: {command['key']}")
