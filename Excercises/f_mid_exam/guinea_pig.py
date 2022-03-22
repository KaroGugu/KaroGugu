
food = float(input())           # quantity food in kilograms
hay = float(input())            # in kilograms
cover = float(input())          # in kilograms
weight = float(input())         # in kilograms

for day in range(1, 30 + 1):
    food -= 0.300              # Every day Puppy eats 300 gr of food

    if day % 2 == 0:
        hay -= food * 0.05

    if day % 3 == 0:
        cover -= weight / 3

if min(food, hay, cover) > 0.001:   # food, hay, and cover, will be enough for a month
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")