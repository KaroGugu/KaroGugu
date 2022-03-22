command = input()

company = {}

while not command == "End":
    current_command = command.split(" -> ")
    company_name = current_command[0]
    employee_id = current_command[1]

    if company_name not in company.keys():  # company still doesn't exist
        company[company_name] = []

    if employee_id not in company[company_name]:
        company[company_name].append(employee_id)  # Add each employee to the given company


    command = input()

# order the companies by name in ascending oreder
# for (company, employee_id) in sorted(company.items(), key=lambda kvp: kvp[0]):
#     print(company)

for company, employee_id in company.items():
    print(company)

    for employ_id in employee_id:
        print(f"-- {employ_id}")