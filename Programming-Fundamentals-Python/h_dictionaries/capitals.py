countries = input().split(", ")    # keys list
capitals = input().split(", ")     # values list


country_capital = dict(zip(countries, capitals))   # dictionary

for (country, capital) in country_capital.items():
    print(f"{country} -> {capital}")

