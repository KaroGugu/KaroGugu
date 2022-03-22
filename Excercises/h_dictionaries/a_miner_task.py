resorces = {}

while True:
    resorce = input()
    if resorce == "stop":
        break
    else:
        quantity = int(input())
        if resorce not in resorces:
            resorces[resorce] = 0

        resorces[resorce] += quantity


for item, number in resorces.items():
    print(f"{item} -> {number}")