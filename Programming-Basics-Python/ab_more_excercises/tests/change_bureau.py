bitcoin = int(input())
ions = float(input())
commision = float(input()) / 100

bitcoint_to_lev = bitcoin * 1168               # Петър си е купил биткойн.
ion_to_dollar = ions * 0.15
dollar_to_lv = ion_to_dollar * 1.76

# euro_lv = 1.95
money_in_lv = bitcoint_to_lev + dollar_to_lv
money_in_euro = money_in_lv / 1.95              # Сега му трябва евро
commision *= money_in_euro
total_sum = money_in_euro - commision

print(f"{total_sum:.2f}")
