price_vegetables = float(input())     # in lv     # зеленчуци за N лева на килограм
price_fruits = float(input())         # in lv     # плодове за M лева за килограм
kilo_vegetables = int(input())
kilo_fruits = int(input())

vegetables = price_vegetables * kilo_vegetables   # still in lv
fruits = price_fruits * kilo_fruits               # still in lv

# да пресмята приходите от реколтата в евро
# 1 евро = 1.94 лв.
total_sum = (vegetables + fruits) / 1.94
print(total_sum)
