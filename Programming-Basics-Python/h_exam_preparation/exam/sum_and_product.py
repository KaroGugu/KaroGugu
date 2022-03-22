n = int(input())

counter = 0
number_reached = False

for a in range(1, 9 + 1):
    for b in range(9, a, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):

                sum = a + b + c + d
                product = a * b * c * d

                if (sum == product) and (n % 10 == 5):
                    counter += 1
                    number_reached = True
                    print(f"{a}{b}{c}{d}")
                    break

                elif (product // sum == 3) and (n % 3 == 0):
                    counter += 1
                    number_reached = True
                    print(f"{d}{c}{b}{a}")
                    break

            if number_reached:
                break
        if number_reached:
            break

    if number_reached:
        break

if counter == 0:
    number_reached = False
    print("Nothing found")