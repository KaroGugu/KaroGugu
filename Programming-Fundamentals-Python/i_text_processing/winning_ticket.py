def is_winning(ticket):
    if len(ticket) != 20:  # A valid ticket has exactly 20 characters.
        return "invalid ticket"

    left_half = ticket[:10]
    right_half = ticket[10:]

    winning_characters = ['@', '#', '$', '^']
    # winning - containing one of the symbols uninterruptedly repeated at least 6 times in both halves of the tickets
    # Jackpot - contain the same winning symbol 10 times on both sides

    for winning_char in winning_characters:
        for repetition in range(10, 5, -1):
            character_repetition = winning_char * repetition
            if character_repetition in left_half and character_repetition in right_half:
                if repetition == 10:  # Jackpot
                    return f'ticket "{ticket}" - {len(character_repetition)}{winning_char} Jackpot!'
                elif 6 <= repetition <= 9:  # Winning ticket
                    return f'ticket "{ticket}" - {len(character_repetition)}{winning_char}'

    return f'ticket "{ticket}" - no match'


tickets = [s.strip() for s in input().split(", ")]   # separated by commas and spaces => we remove spaces

ticket_state = []

for ticket in tickets:
    ticket_state.append(is_winning(ticket))

print("\n".join(ticket_state))