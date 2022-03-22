budget = float(input())
season = input()

destination = ""
camp_or_hotel = ""
money_spent = 0
holiday_information = ''

if season == "summer":
    camp_or_hotel = "camp"
elif season == "winter":
    camp_or_hotel = "winter"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = 0.30 * budget
        holiday_information = f"Camp - {money_spent:.2f}"
    elif season == "winter":
        money_spent = 0.70 * budget
        holiday_information = f"Hotel - {money_spent:.2f}"

elif 100 < budget <= 1000:             # elif budget > 100 and budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = 0.40 * budget
        holiday_information = f"Camp - {money_spent:.2f}"
    elif season == "winter":
        money_spent = 0.80 * budget
        holiday_information = f"Hotel - {money_spent:.2f}"

else:
    destination = "Europe"
    money_spent = 0.90 * budget
    holiday_information = f"Hotel - {money_spent:.2f}"

print("Somewhere in " + destination)
print(holiday_information)
