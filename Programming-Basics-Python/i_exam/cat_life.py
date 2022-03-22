from math import floor
type_of_cat = input()
sex_of_cat = input()

# като 6 човешки месеца се равняват на 1 котешки месец

age = 0

if sex_of_cat == "m":
    if type_of_cat == "British Shorthair":
        age += 13
    elif type_of_cat == "Siamese":
        age += 15
    elif type_of_cat == "Persian":
        age += 14
    elif type_of_cat == "Ragdoll":
        age += 16
    elif type_of_cat == "American Shorthair":
        age += 12
    elif type_of_cat == "Siberian":
        age += 11
    else:
        pass

if sex_of_cat == "f":
    if type_of_cat == "British Shorthair":
        age += 14
    elif type_of_cat == "Siamese":
        age += 16
    elif type_of_cat == "Persian":
        age += 15
    elif type_of_cat == "Ragdoll":
        age += 17
    elif type_of_cat == "American Shorthair":
        age += 13
    elif type_of_cat == "Siberian":
        age += 12
    else:
        pass

age_into_human = age * 12
age_into_cat = age_into_human / 6
age_into_cat = floor(age_into_cat)


if type_of_cat in "British Shorthair" "Siamese" "Persian" "Ragdoll" "American Shorthair" "Siberian":
    print(f"{age_into_cat} cat months")
else:
    print(f"{type_of_cat} is invalid cat!")