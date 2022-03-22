import phonenumbers

from phonenumbers import geocoder, timezone, carrier

number = "+359876292839"

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.describtion_for_number(ch_number, "en"))

ch_number = phonenumbers.parse(number, "BG")
print(carrier.name_for_number(ch_number, "en"))

ch_number = phonenumbers.parse(number)
print(timezone.time_zones_for_number(ch_number))