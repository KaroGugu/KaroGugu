price_for_vegetable = float(input())   # in lv
price_for_fruits = float(input())      # in lv
kilos_vegetables = int(input())
kilos_fruits = int(input())

# пресмята приходите от реколтата в евро ;    1евро = 1.94лв
total_price = (price_for_vegetable * kilos_vegetables + price_for_fruits * kilos_fruits) / 1.94
print(f'{total_price:.2f}')
