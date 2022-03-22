nums = [int(element) for element in input().split()]

factor = int(input())

happiness = [element * factor for element in nums]
threshold = sum(happiness) / len(happiness)

happy_employees = [element for element in happiness if element >= threshold]
sad_employees = [element for element in happiness if element < threshold]

happy_message = "Employees are happy!"
sad_message = "Employees are not happy!"

if len(sad_employees) > len(happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(happiness)}. {sad_message}")
else:
    print(f"Score: {len(happy_employees)}/{len(happiness)}. {happy_message}")
