country = input()
instrument = input()

points_for_difficult = 0
points_for_performance = 0

if instrument == "ribbon":
    if country == "Russia":
        points_for_difficult += 9.1
        points_for_performance += 9.4
    elif country == "Bulgaria":
        points_for_difficult += 9.6
        points_for_performance += 9.4
    elif country == "Italy":
        points_for_difficult += 9.2
        points_for_performance += 9.5

elif instrument == "hoop":
    if country == "Russia":
        points_for_difficult += 9.3
        points_for_performance += 9.8
    elif country == "Bulgaria":
        points_for_difficult += 9.55
        points_for_performance += 9.75
    elif country == "Italy":
        points_for_difficult += 9.45
        points_for_performance += 9.35

elif instrument == "rope":
    if country == "Russia":
        points_for_difficult += 9.6
        points_for_performance += 9.0
    elif country == "Bulgaria":
        points_for_difficult += 9.5
        points_for_performance += 9.4
    elif country == "Italy":
        points_for_difficult += 9.7
        points_for_performance += 9.15

# колко процента не им достигат, за да имат максималната оценка, която е 20
total_score = points_for_difficult + points_for_performance
diff_from_max_score = 20 - total_score
percent_diff_from_max_score = (diff_from_max_score / 20) * 100

print(f"The team of {country} get {total_score:.3f} on {instrument}.")
print(f"{percent_diff_from_max_score:.2f}%")