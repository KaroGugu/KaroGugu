bottles_detergent = int(input())

ml_detergent = bottles_detergent * 750
ml_detergent_per_dish = 5
ml_detergent_per_pot = 15

clean_plates = 0
clean_pots = 0
counter = 0
detergent_enough = False

while ml_detergent >= 0 and not detergent_enough:
    command = input()
    if command == "End":
        detergent_enough = True
    else:
        counter += 1
        items = int(command)

        if counter % 3 == 0:
            ml_detergent -= ml_detergent_per_pot * items
            if ml_detergent >= 0:
                clean_pots += items
        else:
            ml_detergent -= ml_detergent_per_dish * items
            if ml_detergent >= 0:
                clean_plates += items

if ml_detergent >= 0:
    print(f"Detergent was enough!")
    print(f"{clean_plates} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {ml_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(ml_detergent)} ml. more necessary!")