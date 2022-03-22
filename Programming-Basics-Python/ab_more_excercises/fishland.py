price_skumria=float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = float(input())

price_palamut = price_skumria + price_skumria * 0.60        # 60% по-скъп от скумрията
price_safrid = price_caca + price_caca * 0.80               # 80% по-скъп от цацата
price_midi = 7.50

palamud = kg_palamud * price_palamut
safrid = kg_safrid * price_safrid
midi = kg_midi * price_midi

total_sum = palamud + safrid + midi                  # Георги решава да ги нагости с паламуд, сафрид и миди
print(f'{total_sum:.2f}')