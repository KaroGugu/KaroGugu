temperature = float(input())

if temperature >= 26.00 and temperature <= 35.00:
    print("Hot")
elif temperature >= 20.10 and temperature <= 25.90:
    print("Warm")
elif temperature >= 15.00 and temperature <= 20.00:
    print("Mild")
elif temperature >= 12.00 and temperature <= 14.90:
    print("Cool")
elif temperature >= 5.00 and temperature <= 11.90:
    print("Cold")

else:
    print("unknown")
