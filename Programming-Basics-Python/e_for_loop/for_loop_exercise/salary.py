number_of_tabs = int(input())
salary = int(input())

penalty = 0
salary_left = salary - penalty

for tab in range(number_of_tabs):
    name_of_tab = input()
    if name_of_tab == "Facebook":
        penalty += 150
        salary_left = salary - penalty
    elif name_of_tab == "Instagram":
        penalty += 100
        salary_left = salary - penalty
    elif name_of_tab == "Reddit":
        penalty += 50
        salary_left = salary - penalty

if salary_left > 0:
    print(salary_left)
else:
    print("You have lost your salary.")