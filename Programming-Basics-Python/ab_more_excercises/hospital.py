period_of_time = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period_of_time + 1):  # обхождаме всички дни в дадения период
    current_patients = int(input())  # За всеки ден прочитаме от конзолата броя на пациентите
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if current_patients > doctors:
        treated_patients += doctors
        untreated_patients += (current_patients - doctors)
    else:
        treated_patients += current_patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")