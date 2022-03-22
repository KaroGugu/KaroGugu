price_for_naylon = 1.50
price_for_paint = 14.50
price_for_diluent = 5.00
price_for_a_bag = 0.40

naylon = int(input())
paint = int(input())
diluvent = int(input())
hours_working = int(input())

# изчислявам парите за материалите + допълнителните 10% от количеството боя и 2 кв.м. найлон, и 0.40 лв. за торбички

money_for_all_materrial = (naylon + 2) * price_for_naylon + (paint + (paint * 10 / 100)) * price_for_paint +\
                          price_for_diluent * diluvent + price_for_a_bag

money_for_worker = ((money_for_all_materrial * 30) / 100) * hours_working

total_sum = money_for_all_materrial + money_for_worker
print(total_sum)


