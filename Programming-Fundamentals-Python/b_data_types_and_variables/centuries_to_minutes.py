centuries = int(input())

# one year has 365.2422 days on average (the Tropical year)

years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")