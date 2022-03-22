number = int(input())

start_number = 1               # отпечатва всички числа  ≤  n от редицата: 1, 3, 7, 15, 31 ....

while start_number <= number:
    print(start_number)
    start_number = (start_number * 2) + 1               # Всяко следващо число се изчислява като умножим предишното с 2 и добавим 1
