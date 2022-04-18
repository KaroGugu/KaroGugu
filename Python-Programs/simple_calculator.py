def addition(first_number, second_number):
    return f"{first_number + second_number:.2f}"


def subtraction(first_number, second_number):
    return f"{first_number - second_number:.2f}"


def multiplication(first_number, second_number):
    return f"{first_number * second_number:.2f}"


def division(first_number, second_number):
    return f"{first_number / second_number:.2f}"


print("Please select an operation from the following:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    user_choice = input("Please enter your choice (from the options 1, 2, 3, or 4): ")

    if user_choice in ("1, 2, 3, 4"):
        number1 = float(input("Please enter your first number: "))
        number2 = float(input("Please enter your second number: "))

        if user_choice == "1":
            print(number1, "+", number2, "=", addition(number1, number2))

        elif user_choice == "2":
            print(number1, "-", number2, "=", subtraction(number1, number2))

        elif user_choice == "3":
            print(number1, "*", number2, "=", multiplication(number1, number2))

        elif user_choice == "4":
            print(number1, "/", number2, "=", division(number1, number2))

        next_calculation = input("Do you want another calculation? (yes/no): ")
        if next_calculation == "no":
            print("Thank you for using this simple calculator. Have a nice day! Bye.")
            break
        if next_calculation != "yes":
            print("Invalid choice! Please choose 'yes' or 'no'.")
            next_calculation = input(" ")
            if next_calculation == "no":
                print("Thank you for using this simple calculator. Have a nice day! Bye.")
                break

    else:
        print("Invalid choice! Please choose from the above options!")