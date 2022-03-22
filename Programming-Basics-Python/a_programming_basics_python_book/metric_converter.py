number = float(input())
start_metric = input().lower()
converted_metric_into = input().lower()

# m = 1000 mm
# m = 100 cm
# m = 0.000621371192 ml
# m = 39.3700787 in
# m = 0.001 km
# m = 3.2808399 ft
# m = 1.0936133 yd

if start_metric == "km":
    number = number / 0.001
elif start_metric == "mm":
    number /= 1000
elif start_metric == "cm":
    number /= 100
elif start_metric == "mi":
    number /= 0.000621371192
elif start_metric == "in":
    number /= 39.3700787
elif start_metric == "ft":
    number /= 3.2808399
elif start_metric == "yd":
    number /= 1.0936133

if converted_metric_into == "ft":
    number *= 3.2808399
elif converted_metric_into == "km":
    number = number * 0.001
elif converted_metric_into == "mm":
    number *= 1000
elif converted_metric_into == "cm":
    number *= 100
elif converted_metric_into == "mi":
    converted_metric_into *= 0.000621371192
elif converted_metric_into == "in":
    number *= 39.3700787
elif converted_metric_into == "yd":
    number *= 1.0936133

print(f"{number}")