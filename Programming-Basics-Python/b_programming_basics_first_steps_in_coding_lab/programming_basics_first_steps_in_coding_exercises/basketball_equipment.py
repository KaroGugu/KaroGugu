annual_tax = int(input())

# кецове – с 40% по-малка цена от годишната такса
price_of_sneakers = annual_tax - (annual_tax * 40 / 100)                   # annual_tax * 0.60      (100 - 40 = 60)

# екип – цената му е 20% по-евтина от тази на кецовете
price_of_dress = price_of_sneakers - (price_of_sneakers * 20 / 100)

# топка – цената ѝ е 1 / 4 от цената на баскетболния екип
price_of_ball = price_of_dress / 4

# аксесоари – цената им е 1 / 5 от цената на баскетболната топка
price_of_accessories = price_of_ball / 5

total_sum = annual_tax + price_of_sneakers + price_of_dress + price_of_ball + price_of_accessories
print(total_sum)
