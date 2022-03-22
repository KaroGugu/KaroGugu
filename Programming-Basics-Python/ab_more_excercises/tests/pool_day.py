from math import ceil

number_of_people = int(input())
tax_entrance = float(input())
price_chair = float(input())               # само 75% от екипа искат шезлонги     # закръгли до по-голямото цяло число
price_umbrella = float(input())            # един чадър стига за двама души       # закръгли до по-голямото цяло число

total_tax_entrance = number_of_people * tax_entrance

number_of_chairs = ceil(0.75 * number_of_people)      # закръгли до по-голямото цяло число
total_chair_price = number_of_chairs * price_chair

number_of_umbrellas = ceil(0.50 * number_of_people)   # закръгли до по-голямото цяло число
total_umbrellas_price = number_of_umbrellas * price_umbrella

total_price = total_tax_entrance + total_chair_price + total_umbrellas_price

print(f"{total_price:.2f} lv.")