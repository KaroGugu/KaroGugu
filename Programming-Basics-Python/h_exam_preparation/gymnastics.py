country = input()
tool = input()

difficulty = 0
evaluation = 0
total_score = 0

if country == "Russia":
    if tool == "ribbon":
        difficulty = 9.10
        evaluation = 9.40
    elif tool == "hoop":
        difficulty = 9.30
        evaluation = 9.80
    elif tool == "rope":
        difficulty = 9.60
        evaluation = 9.00

elif country == "Bulgaria":
    if tool == "ribbon":
        difficulty = 9.60
        evaluation = 9.40
    elif tool == "hoop":
        difficulty = 9.55
        evaluation = 9.75
    elif tool == "rope":
        difficulty = 9.50
        evaluation = 9.40

elif country == "Italy":
    if tool == "ribbon":
        difficulty = 9.20
        evaluation = 9.50
    elif tool == "hoop":
        difficulty = 9.45
        evaluation = 9.35
    elif tool == "rope":
        difficulty = 9.70
        evaluation = 9.15

total_score = difficulty + evaluation
# каква е оценката на дадена държава за определен уред и колко процента не им достигат,
# за да имат максималната оценка, която е 20
diff = 20 - total_score
needed_percent = (diff / 20) * 100


print(f"The team of {country} get {total_score:.3f} on {tool}.")
print(f"{needed_percent:.2f}%")